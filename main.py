#! /usr/bin/env python

import curses

try:
    stdscr=curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    try:
        curses.start_color()
        canColor=True
    except:
        canColor=False
        pass

    # ---
    stdscr.addstr('%s*%s' % (curses.LINES, curses.COLS))
    stdscr.refresh()
    curses.napms(500)
    stdscr.erase()
    stdscr.addstr(0,0,'Using python on terminal to normal IO operations')
    stdscr.addstr(1,0,'Exit now')
    stdscr.move(0,0)
    nowchoose=0
    while True:
        match stdscr.getch():
            case curses.KEY_DOWN if not nowchoose>=1:
                nowchoose+=1
                stdscr.move(nowchoose,0)
                pass
            case curses.KEY_UP if not nowchoose<=0:
                nowchoose-=1
                stdscr.move(nowchoose,0)
                pass
            case 10:
                break
            case _:
                # Ignored
                pass
        pass
    stdscr.erase()
    match nowchoose:
        case 0:
            #stdscr.addstr(0,0,"This function isn't implemented. Press any key to exit.")
            #stdscr.addstr(1,0,'该功能未实现。按下任意键以退出。')
            #stdscr.addstr(2,0,'この機能は実装されていません。任意のキーを押して終了します。')
            file={}
            match stdscr.getch():
                case ord('s'):
                    with open():
                        pass
        case 1:
            pass
        case _:
            stdscr.addstr(0,0,"FATAL ERROR:Select value not in options. Please feedback the error back to developers. Press any key to exit.")
            stdscr.addstr(1,0,'严重错误：选择选项之外的值。请将此错误反馈给开发人员。按下任意键以退出。')
            stdscr.addstr(2,0,'重大なエラ：オプジョンいがいの値を選択します。このエラを開発者にフィドバックしてください。任意のキーを押して終了します。')
            stdscr.getch()
    # ---

finally:
    if 'stdscr' in locals():
        stdscr.keypad(False)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
