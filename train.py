from roboflow import Roboflow
from ultralytics import YOLO
import os


rf = Roboflow(api_key="fNjcQUWf2aUIjPCKEe1r")
project = rf.workspace("namans-workspace-bmh19").project("safe-mob")
dataset = project.version(1).download("yolo26")

# Larger model = higher ceiling on accuracy at some inference-speed cost.
# Use 'm' if you need real-time speed; 'l' if you can spend a few more ms/frame.
model = YOLO("yolo26m.pt")

model.train(
    data=f"{dataset.location}/data.yaml",
    epochs=300,              # let it actually converge
    patience=50,             # was 4 — this was killing training early
    imgsz=640,               # bump to 960/1280 if objects are small
    batch=-1,                # autobatch: fills GPU memory instead of guessing 8
    device=0,
    workers=8,

    # Optimizer / schedule
    optimizer="AdamW",
    lr0=0.001,
    lrf=0.01,
    cos_lr=True,
    weight_decay=0.0005,
    warmup_epochs=5,

    # Augmentation — tune based on how much variation is in your real deployment scenes
    mosaic=1.0,
    mixup=0.1,
    copy_paste=0.1,
    degrees=10.0,
    translate=0.1,
    scale=0.5,
    fliplr=0.5,
    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4,

    # Loss weighting — nudge up if precision matters more than recall for your use case
    cls=0.5,
    box=7.5,

    val=True,
    plots=True,
    save=True,
    seed=0,
)

# After training: check per-class precision/recall, not just mAP
metrics = model.val()
print(metrics.box.p)     # precision per class
print(metrics.box.r)     # recall per class
print(metrics.box.map50) # mAP@0.5