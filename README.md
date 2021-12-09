# gait_speed_prediction

Predict gait speed using ML / deep learning techniques from wearable sensor data

Background:
https://mueller-et-al-2019.s3.amazonaws.com/independent_validation_study/datasets-validation.pdf

* Study subjects:

  * \>=60 years old
  * walking speed 0.4-0.79 m/s inclusive
  * No. of subjects ~ 25
* Study Parcours:

  * \~250 m including stairs
  * 50 up/down steps stairs or elevator
  * inside/outside/carpet/concrete
  * could be skipped occasionally
  * annotated section codes with entering/leaving time stamps
  * time-stamped event occurance (actibelt data shall be ommited when an event occurs)
* Sensors:

  * Patient-worn actibelt @ 100Hz
  * Wheel-mounted actibelt @ 100Hz
  * Smart phone video @ 120 or 30 FPS
* Sensors synchronization: Manually tapping both sensors using a pen, recording signatures, compensating for signature offset
* Walking Speed Reference from distance and time per quarter wheel revolution
* Synchnronization Methodology:

  * For each row in sync.csv, fetch the corresponding samples recorded by the inertial sensor affixed to the subject's waist from raw.h5. This will result in expanded sync data.
  * For each sample in  the expanded sync data, obtain the synchronized timing for the wheel using the equation:
    * wheel time stamp  = subject start time stamp in sync.csv (subject.start) - subject.delta/100
  * For each obtained wheel time stamp above, look up the nearest time value using 'mid' column in wheel.csv and update the expanded sync data accordingly.
  * Clean long lead and lag trains in addition to faulty speed values e.g. 'inf'

# Installation:

1. Install the environment based on environment.yml
2. In your project root folder, manually create athe folder 'data' and download independent_validation data from the link below using the same folder structure

https://mueller-et-al-2019.s3.amazonaws.com/index.html

Structure:

* data/dervied_data/---
* data/raw_data/---

The data folder will include prcoessed data as well
