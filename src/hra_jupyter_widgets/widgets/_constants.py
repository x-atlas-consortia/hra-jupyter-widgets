import enum


class HraTraitType(enum.StrEnum):
    Attribute = "attribute"
    Event = "event"


class ModelKey(enum.StrEnum):
    TagName = "_tag_name"
    Scripts = "_scripts"
    Styles = "_styles"
    Attributes = "_attributes"
    Events = "_events"


class AttributeBindingKey(enum.StrEnum):
    AttributeName = "attribute_name"
    ModelKey = "model_key"


class EventBindingKey(enum.StrEnum):
    EventName = "event_name"
    Properties = "properties"
