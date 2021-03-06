from logging import debug, info, warning, error, exception

import services
from dbMySql.models import UnprocessedShow, UnprocessedStream, ShowType, str_to_showtype


def main(config, db, *args, **kwargs):
    if len(args) == 1:
        if _edit_with_file(db, args[0]):
            info("Edit successful; saving")
            db.commit()
        else:
            error("Edit failed; reverting")
            db.rollback()
    else:
        warning("Nothing to do")


def _edit_with_file(db, edit_file):
    import yaml

    info("Parsing show edit file \"{}\"".format(edit_file))
    try:
        with open(edit_file, "r", encoding="UTF-8") as f:
            parsed = list(yaml.load_all(f))
    except yaml.YAMLError:
        exception("Failed to parse edit file")
        return

    debug("  num shows={}".format(len(parsed)))

    for doc in parsed:
        name = doc["title"]
        stype = str_to_showtype(doc["type"])  # convert to enum?
        length = doc["length"] if "length" in doc else 0
        has_source = doc["has_source"]

        info("Adding show \"{}\" ({})".format(name, stype))
        debug("  has_source={}".format(has_source))
        if stype == ShowType.UNKNOWN:
            error("Invalid show type \"{}\"".format(stype))
            return False

        show = UnprocessedShow(None, None, name, [], stype, length, has_source)
        found_ids = db.search_show_ids_by_names(name, exact=True)
        if len(found_ids) == 0:
            show_id = db.add_show(show, commit=False)
        elif len(found_ids) == 1:
            show_id = found_ids.pop()
            db.update_show(show_id, show, commit=False)
        else:
            error("More than one ID found for show")
            return False

        # Info
        if "info" in doc:
            infos = doc["info"]
            for info_key in infos:
                url = infos[info_key]
                if not url:
                    continue

                debug("  Info {}: {}".format(info_key, url))
                info_handler = services.get_link_handler(key=info_key)
                if info_handler:
                    info_id = info_handler.extract_show_id(url)
                    debug("    id={}".format(info_id))

                    if not db.has_link(info_key, info_id):
                        show.site_key = info_key
                        show.show_key = info_id
                        db.add_link(show, show_id, commit=False)
                else:
                    error("    Info handler not installed")

        # Streams
        if "streams" in doc:
            streams = doc["streams"]
            for service_key in streams:
                url = streams[service_key]
                if not url:
                    continue
                remote_offset = 0
                try:
                    roi = url.rfind("|")
                    if roi > 0:
                        if roi + 1 < len(url):
                            remote_offset = int(url[roi + 1:])
                        url = url[:roi]
                except:
                    exception("Improperly formatted stream URL \"{}\"".format(url))
                    continue

                info("  Stream {}: {}".format(service_key, url))
                stream_handler = services.get_service_handler(key=service_key)
                if stream_handler:
                    show_key = stream_handler.extract_show_key(url)
                    debug("    id={}".format(show_key))

                    if not db.has_stream(service_key, show_key):
                        s = UnprocessedStream(service_key, show_key, None, "", remote_offset, 0)
                        db.add_stream(s, show_id, commit=False)
                    else:
                        service = db.get_service(key=service_key)
                        s = db.get_stream(service_tuple=(service, show_key))
                        db.update_stream(s, show_key=show_key, remote_offset=remote_offset, commit=False)
                else:
                    error("    Stream handler not installed")

    return True