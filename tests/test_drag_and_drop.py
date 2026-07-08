from playwright.sync_api import expect

from helper_functions.logging import log_debug


def test_drag_and_drop(drag_drop):
    """Verify Element Drag and Drop."""
    drag_drop.drag_and_drop(drag_drop.source, drag_drop.target)
    log_debug(f"Verify element a switch identities with element b.")
    expect(drag_drop.source).to_have_text("B")
    expect(drag_drop.target).to_have_text("A")

    log_debug(f"Verify element a and element b regain initial identities.")
    drag_drop.drag_and_drop(drag_drop.target, drag_drop.source)
    expect(drag_drop.source).to_have_text("A")
    expect(drag_drop.target).to_have_text("B")