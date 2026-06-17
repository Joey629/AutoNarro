"""FastAPI 请求/响应模型。"""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field


class EvaluateRequest(BaseModel):
    text: str = Field(..., min_length=5)
    age: int = Field(..., ge=4, le=12)
    left_behind: int = Field(default=0, ge=0, le=1)
    child_id: str = Field(default="", max_length=64)
    child_name: str = Field(default="", max_length=64)
    class_name: str = Field(default="", max_length=64)
    story_type: Optional[Literal["cat", "dog", "bird", "goat"]] = None
    task_type: Optional[Literal["Telling", "Retelling"]] = None
    coach_mode: Optional[Literal["free", "guided"]] = "free"
    dialogue_log: list[dict] = Field(default_factory=list)


class ParentSurveyRequest(BaseModel):
    answers: dict[str, int] = Field(..., description="question_id -> 1..5")


class StoryCoachGuideRequest(BaseModel):
    phase: str = Field(default="panel_open")
    story_type: str = Field(default="cat")
    story_label: str = Field(default="")
    panel_index: int = Field(default=0, ge=0, le=20)
    panel_total: int = Field(default=6, ge=1, le=20)
    caption: str = Field(default="", max_length=500)
    child_utterance: str = Field(default="", max_length=2000)
    history: list[dict] = Field(default_factory=list)
    use_llm: bool = True


class ExpertOverrideRequest(BaseModel):
    field: str = Field(..., description="pred_SC_Sum（宏观 SC）| micro_sum（宏观 SS 合计）| A2–A16")
    override_value: str
    note: str = ""
    reviewer: str = ""


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    evaluation_id: Optional[int] = None
    history: list[dict] = Field(default_factory=list)


class CoachRequest(BaseModel):
    question: str = ""


class PersonalizedBookGenerateRequest(BaseModel):
    child_id: str = Field(..., min_length=1, max_length=64)
    child_name: str = Field(default="", max_length=64)
    evaluation_ids: list[int] = Field(
        default_factory=list,
        description="可选：指定参与汇总的评估 ID；默认使用该 child_id 下最近若干次已完成评估",
    )


class RecordLabelRequest(BaseModel):
    record_label: str = Field(..., min_length=1, max_length=120)


class FamilyProfileUpdate(BaseModel):
    caregiver_name: str = Field(default="", max_length=64)
    child_name: str = Field(default="", max_length=64)
    child_id: str = Field(default="", max_length=64)
    age: int = Field(default=5, ge=3, le=12)
    gender: str = Field(default="", max_length=16)
    left_behind: int = Field(default=0, ge=0, le=1)
    class_name: str = Field(default="", max_length=64)
    notes: str = Field(default="", max_length=500)


class AuthRegisterRequest(BaseModel):
    email: str = Field(..., min_length=3, max_length=128)
    password: str = Field(..., min_length=8, max_length=128)
    display_name: str = Field(default="", max_length=64)


class AuthLoginRequest(BaseModel):
    email: str = Field(..., min_length=3, max_length=128)
    password: str = Field(..., min_length=1, max_length=128)


class AccountUpdateRequest(BaseModel):
    display_name: str | None = Field(default=None, max_length=64)
    avatar_id: str | None = Field(default=None, max_length=32)
    phone: str | None = Field(default=None, max_length=32)


class ChangePasswordRequest(BaseModel):
    current_password: str = Field(..., min_length=1, max_length=128)
    new_password: str = Field(..., min_length=8, max_length=128)
