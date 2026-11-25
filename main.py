#!/usr/bin/env python3
"""THE BREAKWATER POST — entrypoint (Akun 17, News Image 20261125).

entry.png, berthed beside this file, is the finished page.
This entrypoint ferries it across to /output/entry.png using
plain file descriptors — open, read, write, close — so the
bytes land exactly as they set out. Standard library only.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET_DIR = "/output"
TARGET = os.path.join(TARGET_DIR, "entry.png")


def ferry() -> int:
    os.makedirs(TARGET_DIR, exist_ok=True)
    total = 0
    rfd = os.open(SOURCE, os.O_RDONLY)
    try:
        wfd = os.open(TARGET, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
        try:
            while True:
                block = os.read(rfd, 32768)
                if not block:
                    break
                os.write(wfd, block)
                total += len(block)
        finally:
            os.close(wfd)
    finally:
        os.close(rfd)
    return total


if __name__ == "__main__":
    carried = ferry()
    print(f"ferried {carried} bytes to {TARGET}")
