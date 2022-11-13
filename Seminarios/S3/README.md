Some various things to be taken into account:

- I used Python 3.10, which includes Tkinter version 8.6
- The delivery for the practice includes a report.pdf with the analysis
  required from the Seminar statement.
- The original BBB video I used can be downloaded from:
  http://bbb3d.renderfarming.net/download.html
  I used the 1080p 30fps option for the original.

- All the videos used and created for the practice (original BBB, resolution changes,
  codec changes, stacked comparisons) can be downloaded from this google drive if you
  want to check my work:
  https://drive.google.com/drive/folders/1CABjRT1-Q6Py72Jsq9LulqOMmJASXYTM?usp=sharing
  (could not upload to Github due to size limits and restrictions)
- Those videos were created using CRF = 25 (quality) for all of them, and
  'medium' preset for the HEVC videos. In the VP8 videos a max bitrate
  of 8Mbps was used since it was required to set one according to the FFmpeg guide.
- The following modes were used for each codec:
  - VP8 at Variable Bitrate at constant quality mode.
  - VP9 at Two Pass constant quality mode.
  - HEVC at Constant Rate Factor (constant quality mode).
  - AV1 at Two Pass constant quality mode
Since the codecs don't necessarily have the same modes available for all of them,
I tried to select those that seemed similar to remove variance in the results.
(That's why I chose the modes above, they all have the CRF quality option,
which allows to compare their performance at the same CRF value.)
- Vorbis was used for audio (mainly to just try encoding in another codec, since the
  original video was in AC3, I could have stayed with that and just copy the audio).

- Regarding the structure of the Python project. I first solved each of the tasks
  (change resolution, change codec, stack 4 videos) in traditional fashion using
  console input/output. This corresponds to the files:
  T1_convert_size.py
  T1-2_convert_codec.py
  T1-3_stack_videos.py

  These files can be run standalone to perform the given tasks.
  Then, for the second part with the Tkinter option. You should run main.py, which
  already takes care of everything. For further explanation of the files:
  - tasks_tkinter_UI_handler.py -> Manages the UI for the different options/tasks
  and calls tasks_tkinter.py when necessary.
  - tasks_tkinter.py -> Contains the code with the functions for performing
  the tasks from this seminar. They are very
  similar to the standalone files but with the console input removed
  and some additional Tkinter UI calls. (that's why I decided it was better
  to separate them, it would be a bit of a mess otherwise).
  - utils_tkinter.py -> Contains some small util functions for handling the
  tkinter frame such as clearing it or resizing it.

- Finally, you can also find a sample video in the Google Drive above called
  example.mkv
  where I run the tkinter UI and show the various tasks to show that they work.
  (Video encoded in HEVC using the files of the practice).
