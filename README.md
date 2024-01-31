# Overview
This was an afternoon project to solve an annoyance I had. I loved using Espanso to create little shortcuts to replace words or phrases but I found it no longer worked with 'Mouse Without Borders', which was a major draw for me and led me away from using that application.

I opted to created Pyspand (terrible name), to solve the problem myself by creating phrases in a YAML configuration file with the semi-colon as the entry point. The program would run in the background listening to semi-colon presses and then picking up the word(s) that followed. If it matched what I had in the YAML configuration then it would delete and replace it for me.

To my surprise this actually worked with 'Mouse Without Borders' but I only spent an afternoon on this and never really got back to it. I promise that's why I used 'pass' on the AttributeError catch.

# Packages Used:
- Pillow
- PyAutoGUI
- pynput
- pystray
- PyYAML