---
title: Data surgery is not rocket science
layout: post
---
This is a story of me failing to do something, and some thoughts on how I might have succeeded.

A friend had a problem. He'd been recording some audio on his phone when the battery died, leaving him with a .m4a file that couldn't be played. He had a look at the contents and it contained a bunch of data, so he offered $40 if someone could recover the audio for him.

This seemed like a fun challenge that would exercise skills there isn't much call for. I didn't necessarily expect to succeed, but I decided to give it a go. (I only remember doing something like this once before, when I had a corrupt FAT partition that I managed to fix with some bit-flipping.)

To help, the friend provided two small files from the same app: one a successful recording, and one corrupt like the target file.

The simplest thing was to simply try playing the broken files with mplayer, just in case. It didn't work, and gave an error message saying (among other things) "moov atom not found".

The next thing was to look at all the files in a hex editor, which in this case was "`hexdump -C` piped into less" because I don't think I have a dedicated hex editor installed. I quickly noticed that the good recording had the bytes `moov` at location 0x1d, while the corrupt recordings both had the bytes `free` there.

I also noticed that all three files had the bytes `mdat` at location 0xc95, followed by some low-entropy data, and then some apparently high-entropy data that seemed to go on to the end of the file. I guessed that this was the actual audio data, while the start of the good recording was a valid audio header.

```
00000000  00 00 00 18 66 74 79 70  6d 70 34 32 00 00 00 00  |....ftypmp42....|
00000010  69 73 6f 6d 6d 70 34 32  00 00 0c 79 66 72 65 65  |isommp42...yfree|
00000020  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000c90  00 3f 3f 3f 3f 6d 64 61  74 01 40 22 80 a3 7f f8  |.????mdat.@"....|
00000ca0  85 2d 2d 2d 2d 2d 2d 2d  2d 2d 2d 2d 2d 2d 2d 2d  |.---------------|
00000cb0  2d 2d 2d 2d 2d 2d 2d 2d  2d 2d 2d 2d 2d 2d 2d 2d  |----------------|
*
00000da0  2d 2d 2d 2d 2d 2d 2d 2d  2d 2d 2d 2d 2e ff f1 0a  |------------....|
00000db0  5a 5a 5a 5a 5a 5a 5a 5a  5a 5a 5a 5a 5a 5a 5a 5a  |ZZZZZZZZZZZZZZZZ|
*
00000eb0  5a 5a 5a 5a 5a 5a 5a 5a  5a 5a 5a 5d e0 e2 14 b4  |ZZZZZZZZZZZ]....|
00000ec0  b4 b4 b4 b4 b4 b4 b4 b4  b4 b4 b4 b4 b4 b4 b4 b4  |................|
00000ed0  b4 b4 bc 00 e2 36 2e 70  5b 0c 09 88 8b b1 2a ae  |.....6.p[.....*.|
00000ee0  9d 55 6c 14 4c 2a 2a 55  45 44 01 c5 35 93 14 a0  |.Ul.L**UED..5...|
```

*The start of the target file. `hexdump` prints a `*` to indicate that several lines have been skipped which were identical to the one above. The audio data seems to start around position 0xed2.*

So that gave me another simple thing to try. I took the first 0xc95 bytes from the good file, and byte 0xc95 onwards from the small corrupt file, and concatenated them.

```sh
head -c 3221 tinytest_notbroken.m4a > fixtest-1.m4a
tail -c +3222 tinytest_broken.m4a >> fixtest-1.m4a
```

After this, fixtest-1.m4a played in mplayer. It printed lots of warning messages while it did so, but whatever.

So I did the same thing with the target file, and recovered two seconds of the original audio. I could report to my friend that it started with him saying "um".

This is what I was expecting, since the good recording was only two seconds, and it would presumably have had the length in the header. But now I needed to work out how to lengthen it.

I played around with `ffmpeg`, but it didn't seem to have an option for "ignore the audio duration stated in the header", so it seemed I would have to fix the header myself.

`ftyppm42` seemed like it might be a file type indicator, so I googled that. A few clicks led to [the MP4 registration authority](http://www.mp4ra.org/specs.html#mp4v2), which suggested that the relevant standard was called "ISO/IEC 14496-14". So I then googled "ISO/IEC 14496-14 track header", and found [a pdf of the relevant standard](https://www.cmlab.csie.ntu.edu.tw/~cathyp/eBooks/14496_MPEG4/ISO_IEC_14496-14_2003-11-15.pdf). Unfortunately this is a high-context document, I didn't particularly understand it, and it didn't help me very much.

I also found [wikipedia on MP4](https://en.wikipedia.org/wiki/MPEG-4_Part_14), which pointed me to [ISO base media file format](https://en.wikipedia.org/wiki/ISO_base_media_file_format), ISO/IEC 14496-12. Google then gave me [a pdf of that standard](http://l.web.umkc.edu/lizhu/teaching/2016sp.video-communication/ref/mp4.pdf), which was much more detailed, helpful, and lengthy.

I didn't attempt to understand it all. But I searched for "mdat", and shortly after one of the hits, I found the following description of a data structure:

```
aligned(8) class MovieHeaderBox extends FullBox(‘mvhd’, version, 0) {
    if (version==1) {
        unsigned int(64) creation_time;
        unsigned int(64) modification_time;
        unsigned int(32) timescale;
        unsigned int(64) duration;
    } else { // version==0
        unsigned int(32) creation_time;
        unsigned int(32) modification_time;
        unsigned int(32) timescale;
        unsigned int(32) duration;
    }
    template int(32) rate = 0x00010000; // typically 1.0
    template int(16) volume = 0x0100; // typically, full volume
    const bit(16) reserved = 0;
    const unsigned int(32)[2] reserved = 0;
    template int(32)[9] matrix =
        { 0x00010000,0,0,0,0x00010000,0,0,0,0x40000000 };
        // Unity matrix
    bit(32)[6] pre_defined = 0;
    unsigned int(32) next_track_ID;
}
```

Promising! My header contained the following two lines:

```
00000020  00 00 00 6c 6d 76 68 64  00 00 00 00 d4 6b 4f 0d  |...lmvhd.....kO.|
00000030  d4 6b 4f 0d 00 00 03 e8  00 00 08 17 00 01 00 00  |.kO.............|
```

That's `mvhd` from the description, followed by four null bytes, followed by two identical 32-bit ints - the creation and modification times would naturally have been the same - and then two more ints.

`timescale` was 0x3e8, decimal 1000, which per spec means 1000 time units pass in a second. `duration` was 0x817, decimal 2071, indicating a track 2.071 seconds long. So presumably I need to edit this value.

What to set it to? As long as it's sufficiently long, it's not important. So I set it to 0x10000817, using emacs (in hexl-mode) as my editor, and tried again. No dice, it still cut off at two seconds.

So I searched "duration" in the same file, and found two more places to edit. One soon after the bytes `tkhd`, which used the same timescale as the `mvhd`; and one soon after the bytes `mdhd`, which had its own timescale. In this case the timescale was 0xac44, decimal 44100.

But adding 0x1000000 to both of these durations didn't help either.

(After one of these three edits - I don't remember which - mplayer started reporting the file as being 74 hours long. But it still cut out after two seconds.)

At this point I was up late and out of ideas. But I realized that I could just ask my friend to record another long track, and then use the header from that to do the job. So I left him [instructions](http://pastebin.com/gCaWWWB1), plus some notes on where I'd got to, so someone else could pick up where I'd left off if that didn't work.

Then while I was asleep, someone else came along and fixed it for him before he tried that. I don't know how.

But here are some thoughts on how I might have proceeded, if my friend hadn't been able to record the longer audio.

For one thing, I might have been able to generate my own long file in ffmpeg. But attempting this now, I can't make it work. I [concatenate](https://trac.ffmpeg.org/wiki/Concatenate) several copies of the good recording, and get a file that starts with these three lines:

```
00000000  00 00 00 18 66 74 79 70  4d 34 41 20 00 00 02 00  |....ftypM4A ....|
00000010  69 73 6f 6d 69 73 6f 32  00 00 00 08 66 72 65 65  |isomiso2....free|
00000020  00 07 93 5e 6d 64 61 74  01 40 22 80 a3 7f f8 85  |...^mdat.@".....|
```

It plays fine. But when I try to mix it with the target file, it doesn't play. It complains about the missing moov atom, even though that's also missing in the working concatenated file. I'm not sure what's wrong.

Failing that, I could have recorded the long file myself in the same app my friend used, to spare his attention for things he actually wanted to be doing. (Which, after all, was the reason he was willing to pay someone else to fix the file.) I could also, for curiousity's sake, have recorded another short file, and attempted to find more durations by comparing the headers.

But perhaps the simplest thing would have been to take a completely different approach from the beginning. It turns out that other people have encountered this problem before, and paved the way for those like me. For example, someone on facebook posted [this page](http://sysfrontier.com/en/2014/12/31/hello-world/), which teaches you to fix these files using a piece of software called "faad.exe". More research reveals that this is [open source](http://www.audiocoding.com/index.html), and even available in portage.

(I also find references to FAAD if I google "fix corrupt m4a file".)

It looks like this was a case of "more haste, less speed". At least the haste was fun, but probably not worth the $40 I might have earned by being thorough.
