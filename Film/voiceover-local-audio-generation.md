## Works in terminal

Make sure the audio works

```sh
# Say speaks
say "Text to speak"
# Say speaks with personal voice
say -v LoiTwo "text to speak"

# This command create the file. The file also plays without issue.
say "Text to speak" -o output.wav  --data-format=LEF32@22050

# Both of these commands create the file, but it's silent.
say -v LoiTwo "Text to speak. Hello World I'm a lot of things. A developer...." -o output-loi.wav  --data-format=LEF32@22050
# Ditto
say -v LoiTwo "text to speak" -o output-loi.wav  --file-format='AIFF' && lame -m m output-loi.wav output-loi.mp3
```

## Record System Audio while listening to Audio with Airpods

    - Quicktime: 16 Ch as recording input
    - Sound: Output - Multi 16 channel - Type: Aggregate device
    - Sound: Input - Black Hole 16ch - Type: Virtual

- Turn on quicktime audio recording
- Run say -v LoiTwo "...text..." from terminal
- Check it works.
