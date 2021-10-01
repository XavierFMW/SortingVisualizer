from random import shuffle
import pygame
import sys

WINDOW_WIDTH, WINDOW_HEIGHT = 1530, 850  
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()

int_list = list(range(0, 1530))
shuffle(int_list)


def get_color(num):

    colors = [(255, num, 0), (255 - (num - 255), 255, 0), (0, 255, num - 510), (0, 255 - (num - 765), 255), (num - 1020, 0, 255), (255, 0, 255 - (num - 1275))]
    return colors[num // 255]


def render_list(arr):

  for index, item in enumerate(arr):

    rect = pygame.Rect(index + 1, 0, 1, WINDOW_HEIGHT)
    pygame.draw.rect(WINDOW, get_color(item), rect)

  pygame.display.update()


def check_events():

  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        sys.exit()

    elif event.type == pygame.QUIT:
      sys.exit()


def quick_sort(group, left=0, right=-1):

  if right < 0:
    right = len(group) - 1

  if left >= right:
    return

  pivot = group[right]
  lessThan = left - 1

  for num in range(left, right):

    check_events()

    if group[num] < pivot:

      lessThan += 1
      group[lessThan], group[num] = group[num], group[lessThan]

    render_list(int_list)

  group[right], group[lessThan + 1] = group[lessThan + 1], group[right]

  pivot =  lessThan + 1

  quick_sort(group, left, pivot - 1)
  quick_sort(group, pivot + 1, right)


def bubble_sort(group):

  while True:

    for index, num in enumerate(group):

      check_events()

      if index != len(group) - 1 and num > group[index + 1]:
        group[index], group[index + 1] = group[index + 1], group[index]

      render_list(group)


def insertion_sort(group):

  for index, num in enumerate(group):

    render_list(group)
    check_events()

    try:
      if index != len(group) - 1 and num < group[index - 1]:
        group[index], group[index - 1] = group[index - 1], group[index]

        sub_comparisons = 2
        compare = True

        while compare:

          render_list(group)
          check_events()

          try:
            if index != len(group) - 1 and num < group[index - sub_comparisons]:
              group[index - (sub_comparisons - 1)], group[index - sub_comparisons] = group[index - sub_comparisons], group[index - (sub_comparisons - 1)]
              sub_comparisons += 1
              
            else:
              compare = False

          except IndexError:
            compare = False
    
    except IndexError:
      pass


def selection_sort(group):

  for unsorted_index, x in enumerate(group):

    min_index = unsorted_index

    for index, item in enumerate(group):

      render_list(group)
      check_events()

      if item < group[min_index] and index >= unsorted_index:
        min_index = index

    group[unsorted_index], group[min_index] = group[min_index], group[unsorted_index]
    print(group, "\n")


render_list(int_list)
quick_sort(int_list)
