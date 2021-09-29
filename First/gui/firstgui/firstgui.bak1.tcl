#############################################################################
# Generated by PAGE version 4.10
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

vTcl:font:add_GUI_font font10 \
"-family {DejaVu Sans Mono} -size 12 -weight normal -slant roman -underline 0 -overstrike 0"
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#############################################################################
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    set site_4_0 .top37.pNo41.t0 
    set site_4_0 $site_4_0
    set site_6_0 .top37.pNo41.t0.tPa45.p1 
    set site_6_0 $site_6_0
    set site_7_0 $site_6_0.scr39

    #Updating ttreeview attributes
    .top37.pNo41.t0.tPa45.p1.scr39.01 configure\
        -columns  Col1\
        -height  4

    #heading options.
    .top37.pNo41.t0.tPa45.p1.scr39.01 heading Col1 \
             -text "Col1" \
             -anchor center
    #heading options.
    .top37.pNo41.t0.tPa45.p1.scr39.01 heading #0 \
             -text "Tree" \
             -anchor center
    #column options.
    .top37.pNo41.t0.tPa45.p1.scr39.01 column Col1 \
             -width 203 \
             -minwidth 20 \
             -stretch 1 \
             -anchor w
    #column options.
    .top37.pNo41.t0.tPa45.p1.scr39.01 column #0 \
             -width 203 \
             -minwidth 20 \
             -stretch 1 \
             -anchor w
    set site_6_1 .top37.pNo41.t0.tPa45.p2 
    set site_6_0 $site_6_1
    set site_4_1 .top37.pNo41.t2 
    set site_4_0 $site_4_1
    set site_5_0 $site_4_0.can57
    set site_7_0 .top37.pNo41.t2.can57.tPa58.p1 
    set site_7_1 .top37.pNo41.t2.can57.tPa58.p2 
    set site_4_2 .top37.pNo41.t3 
    set site_4_3 .top37.pNo41.t1 
    set site_4_4 .top37.pNo41.t4 
    set site_3_0 $base.m50
    set site_3_0 $base.m50
    set site_3_0 $base.m50
    set site_3_0 $base.m50
    set site_3_0 $base.m50
    set site_3_0 $base.m50
    set site_3_0 $base.scr38
    set site_3_0 $base.scr39
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m50" -background {#d9d9d9} -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 602x447+987+236
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3271 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel 1"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    ttk::style configure PC.TNotebook -background #d9d9d9
    ttk::style configure PC.TNotebook.Tab -background #d9d9d9
    ttk::style configure PC.TNotebook.Tab -foreground #000000
    ttk::style configure PC.TNotebook.Tab -font TkDefaultFont
    ttk::style layout PC.TNotebook.Tab {
                    Notebook.tab -children {
                        Notebook.padding -side top -children {
                            Notebook.focus -side top -children {
                                Notebook.text -side right
                                Notebook.image -side left
                            }
                        }
                    }
               }
    vTcl::widgets::ttk::pnotebook::createCmd $top.pNo41 \
        -width 300 -height 200 -style {"PC.TNotebook"} 
    vTcl:DefineAlias "$top.pNo41" "PNotebook1" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo41 configure -style "PC.TNotebook"
    bind $top.pNo41 <Button-1> {
        button_press
    }
    bind $top.pNo41 <ButtonRelease-1> {
        button_release
    }
    bind $top.pNo41 <Motion> {
        mouse_over
    }
    frame $top.pNo41.t0 \
        -background {#d9d9d9} -highlightcolor black 
    vTcl:DefineAlias "$top.pNo41.t0" "PNotebook1_t0" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo41 add $top.pNo41.t0 \
        -padding 0 -sticky nsew -state normal -text Home -image image2 \
        -compound none -underline -1 
    set site_4_0  $top.pNo41.t0
    button $site_4_0.but42 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text Connect 
    vTcl:DefineAlias "$site_4_0.but42" "DBConnectButton" vTcl:WidgetProc "Toplevel1" 1
    bind $site_4_0.but42 <Button-1> {
        lambda e: dbconnectbtn(e)
    }
    button $site_4_0.but43 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text {Close Connect} 
    vTcl:DefineAlias "$site_4_0.but43" "DBCloseButton" vTcl:WidgetProc "Toplevel1" 1
    bind $site_4_0.but43 <Button-1> {
        lambda e: dbclosebtn(e)
    }
    entry $site_4_0.ent42 \
        -background white -font font10 -foreground {#000000} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black -takefocus True 
    vTcl:DefineAlias "$site_4_0.ent42" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    bind $site_4_0.ent42 <Enter> {
        lambda e: enterbtn(e)
    }
    button $site_4_0.but44 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text Enter 
    vTcl:DefineAlias "$site_4_0.but44" "EntryBTN" vTcl:WidgetProc "Toplevel1" 1
    bind $site_4_0.but44 <Button-1> {
        lambda e: enterbtn(e)
    }
    ttk::style configure TPanedwindow -background #d9d9d9
    ttk::style configure TPanedwindow.Label -background #d9d9d9
    ttk::style configure TPanedwindow.Label -foreground #000000
    ttk::style configure TPanedwindow.Label -font TkDefaultFont
    ttk::panedwindow $site_4_0.tPa45 \
        -orient horizontal -width 200 -height 200 
    vTcl:DefineAlias "$site_4_0.tPa45" "TPanedwindow1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TLabelframe.Label -background #d9d9d9
    ttk::style configure TLabelframe.Label -foreground #000000
    ttk::style configure TLabelframe.Label -font TkDefaultFont
    ttk::style configure TLabelframe -background #d9d9d9
    ttk::labelframe $site_4_0.tPa45.p1 \
        -width 91 -height 200 
    vTcl:DefineAlias "$site_4_0.tPa45.p1" "TPanedwindow1_p1" vTcl:WidgetProc "Toplevel1" 1
    set site_6_0 $site_4_0.tPa45.p1
    ttk::style configure Treeview.Heading -background #d9d9d9
    ttk::style configure Treeview.Heading -font TkDefaultFont
    vTcl::widgets::ttk::scrolledtreeview::CreateCmd $site_6_0.scr39 \
        -background {#d9d9d9} -height 15 -highlightcolor black -width 30 
    vTcl:DefineAlias "$site_6_0.scr39" "Scrolledtreeview1" vTcl:WidgetProc "Toplevel1" 1
    place $site_6_0.scr39 \
        -in $site_6_0 -x 260 -y 90 -width 420 -anchor nw -bordermode ignore 
    $site_4_0.tPa45 add $site_4_0.tPa45.p1 
        
    ttk::style configure TLabelframe.Label -background #d9d9d9
    ttk::style configure TLabelframe.Label -foreground #000000
    ttk::style configure TLabelframe.Label -font TkDefaultFont
    ttk::style configure TLabelframe -background #d9d9d9
    ttk::labelframe $site_4_0.tPa45.p2 \
        -text {Pane 2} -width 109 -height 200 
    vTcl:DefineAlias "$site_4_0.tPa45.p2" "TPanedwindow1_p2" vTcl:WidgetProc "Toplevel1" 1
    set site_6_1 $site_4_0.tPa45.p2
    label $site_6_1.lab42 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$site_6_1.lab42" "Label1" vTcl:WidgetProc "Toplevel1" 1
    message $site_6_1.mes43 \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text Message -width 83 
    vTcl:DefineAlias "$site_6_1.mes43" "Message1" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_6_1.che44 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -justify left -text Check -variable che44 
    vTcl:DefineAlias "$site_6_1.che44" "Checkbutton3" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_6_1.che45 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -justify left -text Check -variable che45 
    vTcl:DefineAlias "$site_6_1.che45" "Checkbutton4" vTcl:WidgetProc "Toplevel1" 1
    spinbox $site_6_1.spi47 \
        -activebackground {#f9f9f9} -background white -font font9 \
        -foreground black -from 1.0 -highlightbackground black \
        -highlightcolor black -increment 1.0 -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black \
        -textvariable spinbox -to 100.0 
    vTcl:DefineAlias "$site_6_1.spi47" "Spinbox1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $site_6_1.rad48 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -justify left -text Radio -variable {} 
    vTcl:DefineAlias "$site_6_1.rad48" "Radiobutton3" vTcl:WidgetProc "Toplevel1" 1
    place $site_6_1.lab42 \
        -in $site_6_1 -x 10 -y 20 -width 86 -relwidth 0 -height 18 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_1.mes43 \
        -in $site_6_1 -x 10 -y 150 -width 83 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_1.che44 \
        -in $site_6_1 -x 10 -y 50 -anchor nw -bordermode ignore 
    place $site_6_1.che45 \
        -in $site_6_1 -x 10 -y 70 -anchor nw -bordermode ignore 
    place $site_6_1.spi47 \
        -in $site_6_1 -x 10 -y 120 -width 80 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_1.rad48 \
        -in $site_6_1 -x 10 -y 90 -anchor nw -bordermode ignore 
    $site_4_0.tPa45 add $site_4_0.tPa45.p2 
        
    place $site_4_0.but42 \
        -in $site_4_0 -x 30 -y 20 -anchor nw -bordermode ignore 
    place $site_4_0.but43 \
        -in $site_4_0 -x 130 -y 20 -anchor nw -bordermode ignore 
    place $site_4_0.ent42 \
        -in $site_4_0 -x 270 -y 20 -anchor nw -bordermode ignore 
    place $site_4_0.but44 \
        -in $site_4_0 -x 500 -y 20 -anchor nw -bordermode ignore 
    place $site_4_0.tPa45 \
        -in $site_4_0 -x 20 -y 60 -width 550 -relwidth 0 -height 180 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $top.pNo41.t2 \
        -background {#d9d9d9} -highlightcolor black 
    vTcl:DefineAlias "$top.pNo41.t2" "PNotebook1_t1" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo41 add $top.pNo41.t2 \
        -padding 0 -sticky nsew -state normal -text Book -image {} \
        -compound none -underline -1 
    set site_4_1  $top.pNo41.t2
    canvas $site_4_1.can57 \
        -background {#d9d9d9} -borderwidth 2 -closeenough 1.0 -height 231 \
        -highlightcolor black -insertbackground black -relief groove \
        -selectbackground {#c4c4c4} -selectforeground black -width 561 
    vTcl:DefineAlias "$site_4_1.can57" "Canvas1" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_1.can57
    ttk::style configure TPanedwindow -background #d9d9d9
    ttk::style configure TPanedwindow.Label -background #d9d9d9
    ttk::style configure TPanedwindow.Label -foreground #000000
    ttk::style configure TPanedwindow.Label -font TkDefaultFont
    ttk::panedwindow $site_5_0.tPa58 \
        -width 200 -height 200 
    vTcl:DefineAlias "$site_5_0.tPa58" "TPanedwindow2" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TLabelframe.Label -background #d9d9d9
    ttk::style configure TLabelframe.Label -foreground #000000
    ttk::style configure TLabelframe.Label -font TkDefaultFont
    ttk::style configure TLabelframe -background #d9d9d9
    ttk::labelframe $site_5_0.tPa58.p1 \
        -text {Pane 1} -width 200 -height 75 
    vTcl:DefineAlias "$site_5_0.tPa58.p1" "TPanedwindow2_p1" vTcl:WidgetProc "Toplevel1" 1
    set site_7_0 $site_5_0.tPa58.p1
    $site_5_0.tPa58 add $site_5_0.tPa58.p1 
        
    ttk::style configure TLabelframe.Label -background #d9d9d9
    ttk::style configure TLabelframe.Label -foreground #000000
    ttk::style configure TLabelframe.Label -font TkDefaultFont
    ttk::style configure TLabelframe -background #d9d9d9
    ttk::labelframe $site_5_0.tPa58.p2 \
        -text {Pane 2} -width 200 -height 125 
    vTcl:DefineAlias "$site_5_0.tPa58.p2" "TPanedwindow2_p2" vTcl:WidgetProc "Toplevel1" 1
    set site_7_1 $site_5_0.tPa58.p2
    $site_5_0.tPa58 add $site_5_0.tPa58.p2 
        
    entry $site_5_0.ent59 \
        -background white -font font10 -foreground {#000000} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_5_0.ent59" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    entry $site_5_0.ent60 \
        -background white -font font10 -foreground {#000000} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_5_0.ent60" "Entry3" vTcl:WidgetProc "Toplevel1" 1
    button $site_5_0.but61 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text Button 
    vTcl:DefineAlias "$site_5_0.but61" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $site_5_0.but62 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text Button 
    vTcl:DefineAlias "$site_5_0.but62" "Button3" vTcl:WidgetProc "Toplevel1" 1
    button $site_5_0.but63 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text Button 
    vTcl:DefineAlias "$site_5_0.but63" "Button4" vTcl:WidgetProc "Toplevel1" 1
    button $site_5_0.but64 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -text Button 
    vTcl:DefineAlias "$site_5_0.but64" "Button5" vTcl:WidgetProc "Toplevel1" 1
    listbox $site_5_0.lis65 \
        -background white -font font10 -foreground {#000000} -height 84 \
        -highlightcolor black -selectbackground {#c4c4c4} \
        -selectforeground black -width 264 
    .top37.pNo41.t2.can57.lis65 configure -font font10
    .top37.pNo41.t2.can57.lis65 insert end text
    vTcl:DefineAlias "$site_5_0.lis65" "Listbox1" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_5_0.che66 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -justify left -text Check -variable che66 
    vTcl:DefineAlias "$site_5_0.che66" "Checkbutton1" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_5_0.che67 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -justify left -text Check -variable che67 
    vTcl:DefineAlias "$site_5_0.che67" "Checkbutton2" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $site_5_0.rad68 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -justify left -text Radio -variable {} 
    vTcl:DefineAlias "$site_5_0.rad68" "Radiobutton1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $site_5_0.rad69 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -foreground {#000000} -highlightcolor black \
        -justify left -text Radio -variable {} 
    vTcl:DefineAlias "$site_5_0.rad69" "Radiobutton2" vTcl:WidgetProc "Toplevel1" 1
    place $site_5_0.tPa58 \
        -in $site_5_0 -x 10 -y 10 -width 240 -relwidth 0 -height 210 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.ent59 \
        -in $site_5_0 -x 280 -y 10 -anchor nw -bordermode ignore 
    place $site_5_0.ent60 \
        -in $site_5_0 -x 280 -y 50 -anchor nw -bordermode ignore 
    place $site_5_0.but61 \
        -in $site_5_0 -x 270 -y 190 -anchor nw -bordermode ignore 
    place $site_5_0.but62 \
        -in $site_5_0 -x 340 -y 190 -anchor nw -bordermode ignore 
    place $site_5_0.but63 \
        -in $site_5_0 -x 410 -y 190 -anchor nw -bordermode ignore 
    place $site_5_0.but64 \
        -in $site_5_0 -x 480 -y 190 -anchor nw -bordermode ignore 
    place $site_5_0.lis65 \
        -in $site_5_0 -x 280 -y 90 -width 264 -relwidth 0 -height 84 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.che66 \
        -in $site_5_0 -x 490 -y 10 -anchor nw -bordermode ignore 
    place $site_5_0.che67 \
        -in $site_5_0 -x 490 -y 30 -anchor nw -bordermode ignore 
    place $site_5_0.rad68 \
        -in $site_5_0 -x 490 -y 50 -anchor nw -bordermode ignore 
    place $site_5_0.rad69 \
        -in $site_5_0 -x 490 -y 70 -anchor nw -bordermode ignore 
    place $site_4_1.can57 \
        -in $site_4_1 -x 10 -y 10 -width 561 -relwidth 0 -height 231 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $top.pNo41.t3 \
        -background {#d9d9d9} -highlightcolor black 
    vTcl:DefineAlias "$top.pNo41.t3" "PNotebook1_t2" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo41 add $top.pNo41.t3 \
        -padding 0 -sticky nsew -state normal -text User -image {} \
        -compound none -underline -1 
    set site_4_2  $top.pNo41.t3
    frame $top.pNo41.t1 \
        -background {#d9d9d9} -highlightcolor black 
    vTcl:DefineAlias "$top.pNo41.t1" "PNotebook1_t3" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo41 add $top.pNo41.t1 \
        -padding 0 -sticky nsew -state normal -text Settings -image image2 \
        -compound none -underline -1 
    set site_4_3  $top.pNo41.t1
    frame $top.pNo41.t4 \
        -background {#d9d9d9} -highlightcolor black 
    vTcl:DefineAlias "$top.pNo41.t4" "PNotebook1_t4" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo41 add $top.pNo41.t4 \
        -padding 0 -sticky nsew -state normal -text About -image {} \
        -compound none -underline -1 
    set site_4_4  $top.pNo41.t4
    ttk::progressbar $top.tPr46
    vTcl:DefineAlias "$top.tPr46" "MProgressbar" vTcl:WidgetProc "Toplevel1" 1
    menu $top.m50 \
        -activebackground {#d8d8d8} -activeforeground {#000000} \
        -background {#d9d9d9} -font font9 -foreground {#000000} -tearoff 0 
    vTcl:DefineAlias "$top.m50" "MainMenu" vTcl:WidgetProc "" 1
    $top.m50 add cascade \
        -menu "$top.m50.men51" -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans} -size 0 -weight normal -slant roman -underline 0 -overstrike 0"] \
        -foreground {#000000} -label File 
    set site_3_0 $top.m50
    menu $site_3_0.men51 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkMenuFont -foreground black -tearoff 0 
    $site_3_0.men51 add command \
        -activebackground {#d8d8d8} -activeforeground {#000000} \
        -background {#d9d9d9} -command {#open_file} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans} -size 0 -weight normal -slant roman -underline 0 -overstrike 0"] \
        -foreground {#000000} -label Open 
    $site_3_0.men51 add command \
        -activebackground {#d8d8d8} -activeforeground {#000000} \
        -background {#d9d9d9} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans} -size 0 -weight normal -slant roman -underline 0 -overstrike 0"] \
        -foreground {#000000} -label Close 
    $top.m50 add cascade \
        -menu "$top.m50.men52" -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans} -size 0 -weight normal -slant roman -underline 0 -overstrike 0"] \
        -foreground {#000000} -label Edit 
    set site_3_0 $top.m50
    menu $site_3_0.men52 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkMenuFont -foreground black -tearoff 0 
    $top.m50 add cascade \
        -menu "$top.m50.men53" -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans} -size 0 -weight normal -slant roman -underline 0 -overstrike 0"] \
        -foreground {#000000} -label Tools 
    set site_3_0 $top.m50
    menu $site_3_0.men53 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkMenuFont -foreground black -tearoff 0 
    $top.m50 add cascade \
        -menu "$top.m50.men54" -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans} -size 0 -weight normal -slant roman -underline 0 -overstrike 0"] \
        -foreground {#000000} -label Database 
    set site_3_0 $top.m50
    menu $site_3_0.men54 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkMenuFont -foreground black -tearoff 0 
    $site_3_0.men54 add command \
        -activebackground {#d8d8d8} -activeforeground {#000000} \
        -background {#d9d9d9} -command {#} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans} -size 0 -weight normal -slant roman -underline 0 -overstrike 0"] \
        -foreground {#000000} -label Open 
    $site_3_0.men54 add command \
        -activebackground {#d8d8d8} -activeforeground {#000000} \
        -background {#d9d9d9} -command {#} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans} -size 0 -weight normal -slant roman -underline 0 -overstrike 0"] \
        -foreground {#000000} -label Close 
    $site_3_0.men54 add separator \
        -background {#d9d9d9} 
    $site_3_0.men54 add command \
        -activebackground {#d8d8d8} -activeforeground {#000000} \
        -background {#d9d9d9} -command {#} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans} -size 0 -weight normal -slant roman -underline 0 -overstrike 0"] \
        -foreground {#000000} -label {Config File} 
    $top.m50 add cascade \
        -menu "$top.m50.men55" -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans} -size 0 -weight normal -slant roman -underline 0 -overstrike 0"] \
        -foreground {#000000} -label Windows 
    set site_3_0 $top.m50
    menu $site_3_0.men55 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkMenuFont -foreground black -tearoff 0 
    $top.m50 add cascade \
        -menu "$top.m50.men56" -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans} -size 0 -weight normal -slant roman -underline 0 -overstrike 0"] \
        -foreground {#000000} -label Help 
    set site_3_0 $top.m50
    menu $site_3_0.men56 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkMenuFont -foreground black -tearoff 0 
    $site_3_0.men56 add command \
        -activebackground {#d8d8d8} -activeforeground {#000000} \
        -background {#d9d9d9} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans} -size 0 -weight normal -slant roman -underline 0 -overstrike 0"] \
        -foreground {#000000} -label About 
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr38 \
        -background {#d9d9d9} -height 75 -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr38" "OutputDisplay" vTcl:WidgetProc "Toplevel1" 1

    $top.scr38.01 configure -background black \
        -font font9 \
        -foreground white \
        -height 3 \
        -highlightcolor yellow \
        -insertbackground blue \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground red \
        -width 10 \
        -wrap none
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr39 \
        -background {#d9d9d9} -height 75 -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr39" "ErrorDisplay" vTcl:WidgetProc "Toplevel1" 1

    $top.scr39.01 configure -background black \
        -font font9 \
        -foreground white \
        -height 3 \
        -highlightcolor black \
        -insertbackground blue \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground red \
        -width 10 \
        -wrap none
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.pNo41 \
        -in $top -x 10 -y 140 -width 582 -relwidth 0 -height 273 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tPr46 \
        -in $top -x 10 -y 420 -anchor nw -bordermode ignore 
    place $top.scr38 \
        -in $top -x 20 -y 10 -width 286 -relwidth 0 -height 123 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.scr39 \
        -in $top -x 300 -y 10 -width 286 -relwidth 0 -height 123 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

  set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
Window show .
Window show .top37 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

