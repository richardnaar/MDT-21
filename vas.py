def present(win, thisExp, esckey, clock, visual, event, core, text_pos, question_text, low, high):
    # mouse = event.Mouse(win=win)
    scale_width = 0.5
    scale_y_pos = -0.1
    text_h = 0.04

    qElem = visual.TextStim(win=win, name='qElem', text='default text',
                            font='Arial', pos=text_pos['slf_txt'], height=text_h, wrapWidth=1.25, ori=0,
                            color=[0.702, 0.702, 0.702], colorSpace='rgb', opacity=1,
                            languageStyle='LTR', depth=-1.0)

    lowElem = visual.TextStim(win=win, name='lowElem',
                              text='default text',
                              font='Arial',
                              pos=text_pos['slf_low'], height=text_h, wrapWidth=1.25, ori=0,
                              color=[0.702, 0.702, 0.702], colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-2.0)

    highElem = visual.TextStim(win=win, name='highElem',
                               text='default text',
                               font='Arial',
                               pos=text_pos['slf_high'], height=text_h, wrapWidth=1.25, ori=0,
                               color=[0.702, 0.702, 0.702], colorSpace='rgb', opacity=1,
                               languageStyle='LTR',
                               depth=-3.0)

    slf_scale = visual.Rect(
        win=win, name='slf_scale',
        width=(scale_width*2), height=(0.05), ori=0, pos=(0, scale_y_pos),
        lineWidth=text_h, lineColor=[0.702, 0.702, 0.702], lineColorSpace='rgb',
        fillColor=[0.702, 0.702, 0.702], fillColorSpace='rgb',
        opacity=1, depth=-4.0, interpolate=True)

    slf_set = visual.Rect(
        win=win, name='slf_set',
        width=(0.01), height=(0.05), ori=0, pos=(0, scale_y_pos),
        lineWidth=text_h, lineColor=[0, 0, 0], lineColorSpace='rgb',
        fillColor=[0, 0, 0], fillColorSpace='rgb',
        opacity=1, depth=-5.0, interpolate=True)

    def draw_VAS(win, question_text, low, high, qElem, lowElem, highElem, slf_scale, slf_set):
        mouse = event.Mouse(win=win)
        # Initialize components for Routine "VAS"
        VAS_startTime = clock.getTime()
        VAS_noResponse = True
        # if button is down already this ISN'T a new click
        prevButtonState = mouse.getPressed()
        mouse.setPos([0, scale_y_pos])
        qElem.setText(question_text)
        lowElem.setText(low)
        highElem.setText(high)

        # if expInfo['test'] == '1':
        #     VAS_noResponse = False
        #     VAS_resp = 'test'
        #     VAS_RT = 0

        while VAS_noResponse:
            # mouse = event.Mouse(win=win)
            if not event.getKeys(esckey):
                # cursor updates
                mx = mouse.getPos()
                mx[1] = scale_y_pos

                if mx[0] <= -scale_width:
                    mx[0] = -scale_width
                elif mx[0] >= scale_width:
                    mx[0] = scale_width

                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        VAS_RT = clock.getTime() - VAS_startTime
                        VAS_resp = ((mx[0]+scale_width)/scale_width)*50
                        VAS_noResponse = False

                # update/draw components on each frame
                qElem.draw(), lowElem.draw(), highElem.draw(), slf_scale.draw()
                # draw cursor
                slf_set.setPos(mx, log=False)
                slf_set.draw()

                # win.flip()
                try:
                    win.flip()
                except:
                    pass

            else:
                core.quit()
        try:
            win.flip()
        except:
            pass
        # win.flip()

        # save the rating and RT
        thisExp.addData('vas_response', VAS_resp)
        thisExp.addData('vas_rt', VAS_RT)
        mouse.setVisible(False)
        core.wait(0.25)

    draw_VAS(win, question_text, low, high, qElem,
             lowElem, highElem, slf_scale, slf_set)


if __name__ == '__main__':
    present()  # Put the a call to the main function in the file.
