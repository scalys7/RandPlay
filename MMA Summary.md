Musical MIDI Accompaniment (MMA)
===================


Musical MIDI Accompaniment, MmA, is a textual format from which standard MIDI files are generated; they most commonly used as a backup track for a soloist.
We will use it in order to programmatically create music!

MmA builds its output based on patterns and sequences supplied by you. These will later define a groove, which transformers a sequence of chords onto the information MmA needs to create music.

Tracks
----------
Tracks represent the musical role of a single instrument. MMA tracks are later mapped onto MIDI tracks, which later differentiate the musical roles and can be used to assign different virtual instruments onto each track, by the MIDI player.

###Track Types###
The basic track types are: ARIA, ARPEGGIO, BASS, CHORD, DRUM, MELODY, SCALE, SOLO, and PLECTRUM.

Musical accompaniment comes in a combination of the following:
 -  Chords played in a rhythmic or sustained manner,
 -  Single notes from chords played in a sustained manner,
 -  Bass notes. Usually played one at a time in a rhythmic manner,
 -  Scales, or parts of scales. Usually as an embellishment,
 -  Single notes from chords played one at time: arpeggios.
 -  Drums and other percussive instruments played rhythmically

###Track Names###
Tracks are named by appending a “-” and “name” to the type-name.
drum tracks, for example, can have names “Drum-1”, “Drum-Loud” or even “Drum-a-long-name”, etc.


Patterns 
------------
A pattern is a definition for a voice or track which describes what rhythm to play during the current bar. The actual notes selected for the rhythm are determined by the *song bar data*.

Patterns can be defined for BASS, WALK, CHORD, ARPEGGIO and DRUM tracks.

###Definition###
Each pattern is defined by the following line:
>> [Track] DEFINE [Position] [Duration] [Volume]

>E.g.,
>>Drum Define S1 1 0 50

 -  A unique label to identify the pattern. This is case-insensitive. 
 -  A series of note definitions. Each set in the series is delimited with a “;”.
 -  When to start the note. This is expressed as a beat offset.
    to start a note at the start of a bar you use “1”, the second beat would be “2”, the fourth     “4”, etc.
 - Note length; e.g., 1 whole, 2 half etc. 
 - Volume - the MIDI velocity to use for the specified note; ranges from 0 to 127.
 - The end of the pattern definition is indicated by the end-of-line.
 
> The pattern names “z” or “Z” and “-” are also reserved.

Sequences
---------------
A SEQUENCE command sets the pattern(s) used in creating each track in your song:
>Track Sequence Pattern1 Pattern2 ...

>“Track” can be any valid track name: “Chord”, “Walk”, “Walk-Sus”, “Arpeggio-88”, etc.
>All pattern names used when setting a sequence need to be defined when this command is issued; or you can use what appears to be a pattern definition right in the sequence command by enclosing the pattern definition in a set of curly brackets “{ }”.

>If there are fewer patterns than SEQSIZE, the sequence will be filled out to correct size. If the number of patterns used is greater than SEQSIZE (see chapter 27) a warning message will be printed and the pattern list will be truncated.

**SeqClear**
This command clears all existing sequences from memory. It is useful when defining a new sequence and you want to be sure that no “leftover” sequences are active.
> SeqClear ;clears all tracks
> [Track] SeqClear ;clears sequences for specified track

Grooves
------------
A groove is just a simple mechanism for saving and restoring a set of patterns and sequences. Using grooves it is easy to create sequence libraries which can be incorporated into your songs with a single command.

### Definition ###
A groove can be created at anytime in an input file with the command
> DefGroove [name] [@opt@ comment]

You can restore a previously defined groove at anytime in your song with:
> Groove [name]

This sets the current groove, that will be used to differ chord sequences onto actual musical arrangement.


Musical Data Format
-----------------------------

### Bar Definition ###
>[@opt@ bar number] Chord [Chord ...] [@opt@ lyric] [@opt@ solo] [* Factor]
>Where factor determines how many times the bar will be repeated.

Chords
----------
One can either specify the absolute, alphabatical chord name, e.g., C, Bm, and B#7.
Alternatively, one could specify scale-relative chords using the Roman notation, e.g., Chord Chords {I / III} / / {V7}.

Tempo And Timing
--------------------------
### Tempo ###
The tempo of a piece is set in Quarter Beats per Minute with the “Tempo” directive.
>Tempo 120

sets the tempo to 120 beats/minute. You can also use the tempo command to increase or decrease the current rate by including a leading “+”, “-” or “*” in the rate. For example,
>Tempo +10

### Time Signature ###
The *Time* command specifies the **Number Of Quarter Notes In A Bar.**
> Time [num quarter notes]

Thus, to specify a 4 by 4 bar, use Time 4; 3 by 4 is Time 3. Fractions is also acceptable, thus a 5 by 8 would by Time 2.5.

Keys
------
A key is defined by the *KeySig* command, such as:
> KeySig E

In MmA it will effect the notes used in SOLO or MELODY tracks, and is a basic requirement for ROMAN numeral chords.