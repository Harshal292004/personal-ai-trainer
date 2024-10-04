# Workout Rep Counter

This application uses computer vision to detect and count workout repetitions in real-time, focusing on arm exercises like bicep curls.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/workout-rep-counter.git
cd workout-rep-counter
```

2. Install the required dependencies:

```bash
pip install -r requirments.txt
```
## Usage

Run the main script:

```bash
python main.py
```

This will open your webcam feed and start tracking your movements.

## Key Features

1. **Real-time Pose Detection**: Uses MediaPipe to detect and track body landmarks.

2. **Angle Calculation**: Calculates angles between key body points (shoulder, elbow, wrist) to determine arm position.

3. **Rep Counting**: Counts repetitions for arm exercises (e.g., bicep curls) based on arm angles.

4. **Bilateral Tracking**: Tracks both left and right arms simultaneously.

5. **Visual Feedback**: Displays rep count, current arm states, and angle measurements on the video feed.

6. **FPS Display**: Shows the current frames per second for performance monitoring.

## How It Works

1. The application captures video from your webcam.
2. It detects body landmarks using the PoseDetector class.
3. Angles between the shoulder, elbow, and wrist are calculated for both arms.
4. The state of each arm (up or down) is determined based on these angles.
5. A rep is counted when a full motion cycle is completed.
6. Real-time information is displayed on the video feed.

## Customization

- Adjust the angle thresholds in the main script to fit different exercises or body types.
- Modify the PoseDetector class parameters for different detection sensitivities.

## Troubleshooting

- Ensure good lighting for accurate pose detection.
- Wear contrasting clothes to your background for better landmark detection.
- If the application runs slowly, try reducing the resolution of your webcam feed.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check
[issues page](https://github.com/Harshal292004/workout-rep-counter/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
