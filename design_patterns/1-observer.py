#!/usr/bin/env python3
from __future__ import annotations
from typing import Protocol


# This is a protocol defining how the *recipient* of an Event broadcasted
#   will process the information received
class Observer(Protocol):
    def update(self, topic: str, data: str) -> None: ...


# This is the orchestrator ("Handler") which will "push" the information
#   But instead of generating an "Event" sent into a stream which would be
#   "catched" by the interested recipients themselves, we use here a pattern
#   where the Handler keeps a list of "interested people" and parses it
#   to call each of them directly.
# Like, instead of having a news broadcast to radio and people who want to
#   hear it will take the initiative of turning their box on, we have
#   the radio speaker individually calling the ones who had expressed
#   their interest beforehand.
class NewsSubject:
    def __init__(self) -> None:
        self._subs: dict[Observer, set[str] | None] = {}

    # Add an "interested person" to its lists of "people to call potentially"
    def subscribe(self, observer: Observer, topics: set[str] | None = None):
        if observer in self._subs:
            return  # ignore duplicate subscribe for same instance
        self._subs[observer] = topics

    # "Interested person" asks to be removed from the list.
    def unsubscribe(self, observer: Observer) -> None:
        self._subs.pop(observer, None)

    # Put a post-it in front of you with the news category and content,
    # Pick registry in left hand, and for each known interested person
    #   check if (s)he is interested in that kind of news, if yes call it
    #   using the same protocol for everyone (let's same mobile phone here).
    def notify(self, topic: str, data: str) -> None:
        for observer, interests in list(self._subs.items()):
            if interests is not None and topic not in interests:
                continue
            observer.update(topic, data)


class LogObserver:
    def update(self, topic: str, data: str) -> None:
        print(f"log:{topic}={data}")


class EmailObserver:
    def update(self, topic: str, data: str) -> None:
        print(f"email:{topic}={data}")


class SmsObserver:
    def update(self, topic: str, data: str) -> None:
        print(f"sms:{topic}={data}")


def main() -> None:
    # Create the radio speaker who will receive all news.
    subject = NewsSubject()
    # Create "interested people" of various profiles
    log = LogObserver()
    email = EmailObserver()
    sms = SmsObserver()

    # Be the "God" which tells the radio speaker that...
    # "M. Log would like to receive breaking news and sport results"
    subject.subscribe(log, topics={"sports", "breaking"})
    # "M. Mail would like to be receive all kind of information"
    subject.subscribe(email)  # None = receives all topics
    # "M. SMS only want the hottest / most important news"
    subject.subscribe(sms, topics="breaking")

    # Be the "God" which tells the radio speaker to inform
    #   about news in different topics.
    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
