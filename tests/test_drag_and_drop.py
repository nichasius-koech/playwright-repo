from playwright.sync_api import expect

from utils.logger import get_logger

logger = get_logger(__name__)


def test_drag_and_drop(drag_drop):
    """Verify Element Drag and Drop."""
    drag_drop.drag_and_drop(drag_drop.source, drag_drop.target)
    logger.debug(f"Verify element a switch identities with element b.")
    expect(drag_drop.source).to_have_text("B")
    expect(drag_drop.target).to_have_text("A")

    logger.debug(f"Verify element a and element b regain initial identities.")
    drag_drop.drag_and_drop(drag_drop.target, drag_drop.source)
    expect(drag_drop.source).to_have_text("A")
    expect(drag_drop.target).to_have_text("B")