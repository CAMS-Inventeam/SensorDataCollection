# Sensor Data Collection

This repository is for testing sensor data collection

## Custom serial protocol

### Begin Message
`DATA_BEGIN` - begins sensor data collection

### End Message
`DATA_END` - finishes collection of a data sample

### Data
`<Variable>: <Value>`

List of variables:
- Heartrate - the user heartrate in BPM
- Confidence - the confidence of the accuracy of the values given in percent
- Oxygen - the blood oxygen level of the user
- Status - the status value from 0-3
