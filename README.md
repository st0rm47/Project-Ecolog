# Project Ecolog

Project Ecolog is a Raspberry Pi-based environmental monitoring system that uses audio and image processing to detect and respond to forest fires. The system includes functionality for detecting gunshots and smoke, triggering actions on external devices, and sending signals to a web application for real-time monitoring.

## Features

- Audio monitoring for gunshot and smoke detection.
- Image capture and processing for forest fire detection.
- Integration with Azure Storage for image upload.
- Integration with Custom Vision API for image classification.
- Buzzer for audio feedback on detection.
- Web API for triggering actions and sending signals.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/st0rm47/Project-Ecolog.git

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

3. Configure Azure Storage connection string and container name in `camera.py` and `main.py`.
4. Configure Custom Vision API endpoint and prediction key in `camera.py` and `main.py`.
5. Set up GPIO pins for buzzer and smoke sensor according to your hardware setup.

## Usage

- Run `main.py` to start the environmental monitoring system.
- Use the `--model`, `--maxResults`, `--overlappingFactor`, and `--scoreThreshold` arguments to customize the audio classification model and its parameters.

## Contributors

- [Subodh Ghimire](https://github.com/st0rm47)
- [Firoj Paudel](https://github.com/firojpaudel)
- [Miraj Bhattarai](https://github.com/mirajb1)
- [Famous Dhungana](https://github.com/prasiddha98)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
