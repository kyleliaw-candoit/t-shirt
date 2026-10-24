# FSRCNN x4 model provenance

Unmodified `FSRCNN_x4.pb`, downloaded October 23, 2026 from Saafke/FSRCNN_Tensorflow:
https://raw.githubusercontent.com/Saafke/FSRCNN_Tensorflow/master/models/FSRCNN_x4.pb

SHA-256: `5c68d18db561aed8ead4ffedf1b897ea615baaf60ebf6c35f8e641f8fa4a21bf`

The accompanying upstream Apache-2.0 license is retained as LICENSE-FSRCNN.txt. The repair script verifies the model digest before loading it. The bundled model is frozen for reproduction even if the upstream branch moves.

OpenCV usage reference: https://docs.opencv.org/4.11.0/d5/d29/tutorial_dnn_superres_upscale_image_single.html
Vector tracing implementation: https://github.com/visioncortex/vtracer

EDSR x4 was benchmarked but not selected: approximately 4.4 seconds for a 64 × 64 input on this CPU. FSRCNN x4 processed a 512 × 512 input in approximately 0.76 seconds and enabled full-image comparisons. This is an efficiency choice, not a claim that FSRCNN universally outperforms EDSR in quality.
