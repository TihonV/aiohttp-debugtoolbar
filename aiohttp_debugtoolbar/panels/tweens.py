from pyramid.interfaces import ITweens

from .base import DebugPanel

_ = lambda x: x


class TweensDebugPanel(DebugPanel):
    """
    A panel to display the tweens used by your Pyramid application.
    """
    name = 'Tweens'
    has_content = True
    template = 'tweens.dbtmako'
    title = _('Tweens')
    nav_title = title

    def __init__(self, request):
        super().__init__(request)
        if not request.app.middlewares:
            self.has_content = False
            self.is_active = False
        else:
            self.populate(request)

    def populate(self, request):
        # TODO: fix this works only for functions and classes
        tweens = [t.__name__ for t in request.app.middlewares]
        self._data = {'tweens': tweens}