from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_rules(self) -> "AlienContact":
        if (self.contact_id[0] != "A" or self.contact_id[1] != "C"):
            raise ValueError("Contact ID must start with AC")
        if (self.contact_type == ContactType.telepathic):
            if (self.witness_count < 3):
                raise ValueError(
                    "Telepathic contact requires"
                    " at least 3 witnesses"
                    )
        if (self.contact_type == ContactType.physical):
            if (self.is_verified is False):
                raise ValueError("Physical contact reports must be verified")
        if (self.signal_strength > 7.0):
            if (self.message_received is None):
                raise ValueError("Strong signals require a message")
        return (self)


def main() -> None:

    print("Alien Contact Log Validation")
    print("======================================")

    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.fromisoformat("2024-01-01T12:00:00"),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=False
    )

    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")

    print()
    print("======================================")

    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.fromisoformat("2024-01-01T12:00:00"),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=6.0,
            duration_minutes=30,
            witness_count=1,
            message_received=None,
            is_verified=False
        )

    except ValueError:
        print("Expected validation error:")
        print("Telepathic contact requires at least 3 witnesses")


if __name__ == "__main__":
    main()
