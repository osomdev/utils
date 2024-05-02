#!/usr/bin/env pyshrimp
# $requires: click==8.0.4

from click import style
import click
import hashlib
import math


@click.command()
@click.option('--text', required=True, prompt='Text')
@click.option('-n', '--num-parts', type=int, default=5)
@click.option('--ignore-space/--no-ignore-space', type=bool, default=True)
@click.option('--checksum', is_flag=True)
def letter_split(text, num_parts, ignore_space, checksum):
    text_to_split = text
    if ignore_space:
        text_to_split = text_to_split.replace(' ', '')

    parts = [[] for _ in range(num_parts)]
    for idx, letter in enumerate(text_to_split):
        parts[idx % num_parts].append(letter)

    for part in parts:
        part_str = ''.join(part)
        if checksum:
            part_str_checksum = hashlib.sha1(part_str.encode('utf-8')).hexdigest()
            pad_len = math.ceil(len(text_to_split) / num_parts)
            part_str_pad = part_str.ljust(pad_len, ' ')
            print(f'{style(part_str_pad, bold=True)}    {part_str_checksum}')
        else:
            print(part_str)


if __name__ == "__main__":
    letter_split()
