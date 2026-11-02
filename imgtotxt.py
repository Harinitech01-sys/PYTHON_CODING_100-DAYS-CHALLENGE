
import torch
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained(
    "segmind/tiny-sd", torch_dtype=torch.float32
)
pipe = pipe.to("cpu")

prompt = input("Enter image prompt: ")
image = pipe(prompt, num_inference_steps=20).images[0]
image.save("generated_image.png")
image.show()
print("Image generated successfully!")
