# Kingdom Hearts: Trading Card Game

Hopefully making a kingdom hearts TCG application

## NEXT STEPS:

I realized that the way I am currently working won't work. I am going to have to move tkinter into the main thread, with socket still being threaded I guess. I am thinking of having something that checks if a queue is empty, and if it isn't then it calls a function.