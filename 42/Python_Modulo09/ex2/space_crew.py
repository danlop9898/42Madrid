from pydantic import BaseModel, Field, ValidationError
from pydantic import model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=1, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    budget_millions: float = Field(ge=1.0, le=10000.0)
    crew: list[CrewMember]
    mission_status: str = Field(default="planned")

    @model_validator(mode="after")
    def check_rules(self) -> "SpaceMission":
        if (self.mission_id[0] != "M"):
            raise ValueError("Mission ID must start with M")

        has_leader = False
        for member in self.crew:
            if member.rank in (Rank.captain, Rank.commander):
                has_leader = True
        if not has_leader:
            raise ValueError(
                "Mission must have at least one"
                " Commander or Captain"
            )

        if self.duration_days > 365:
            total = len(self.crew)
            experienced = 0

            for member in self.crew:
                if member.years_experience >= 5:
                    experienced += 1

            if experienced < total / 2:
                raise ValueError("Long missions require 50% experienced crew")

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:

    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2024-01-01T12:00:00"),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=35,
                    specialization="Mission Command",
                    years_experience=10
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=30,
                    specialization="Navigation",
                    years_experience=10
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=28,
                    specialization="Engineering",
                    years_experience=3
                )
            ]
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")

        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value}) -"
                f"{member.specialization}"
                )

        print("=========================================")

    except ValidationError:
        print("Expected validation error:")
        print("Mission must have at least one Commander or Captain")

    try:
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Test Mission Failure",
            destination="Mars",
            launch_date=datetime.fromisoformat("2024-01-01T12:00:00"),
            duration_days=100,
            budget_millions=1000.0,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Test One",
                    rank=Rank.lieutenant,
                    age=30,
                    specialization="Navigation",
                    years_experience=2
                ),
                CrewMember(
                    member_id="C002",
                    name="Test Two",
                    rank=Rank.officer,
                    age=28,
                    specialization="Engineering",
                    years_experience=3
                )
            ]
        )

    except ValidationError:
        print("Expected validation error:")
        print("Mission must have at least one Commander or Captain")


if __name__ == "__main__":
    main()
