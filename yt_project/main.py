from yt_project.pipeline.steps.get_video_list import GetVideoList
from yt_project.pipeline.steps.step import StepException

from yt_project.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCL_qhgtOy0dy1Agp8vkySQg'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
