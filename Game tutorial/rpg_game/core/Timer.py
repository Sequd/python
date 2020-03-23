import pygame
from Constants import *


class Timer:
    def __init__(self, screen):
        self.screen = screen

        # Loop until the user clicks the close button.
        self.done = False

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 25)

        self.frame_count = 0
        self.frame_rate = FPS
        self.start_time = 90

    def update(self):
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = self.frame_count // self.frame_rate

        # Divide by 60 to get total minutes
        minutes = total_seconds // 60

        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60

        # Use python string formatting to format in leading zeros
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

        # Blit to the screen
        self.first_text = self.font.render(output_string, True, RED, BLACK)

        # --- Timer going down ---
        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = self.start_time - (self.frame_count // self.frame_rate)
        if total_seconds < 0:
            total_seconds = 0

        # Divide by 60 to get total minutes
        minutes = total_seconds // 60

        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60

        # Use python string formatting to format in leading zeros
        output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)

        # Blit to the screen
        self.text = self.font.render(output_string, True, RED, BLACK)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        self.frame_count += 1
        # Limit frames per second
        # self.clock.tick(self.frame_rate)

    def render(self):
        self.screen.blit(self.first_text, [10, 10])
        self.screen.blit(self.text, [10, 40])
