#!/usr/bin/env python

from geocamTrack.models import Track, LineStyle, IconStyle

# hex abgr
COLORS = ['ff0000ff',  # red
          'ffff00ff',  # magenta
          'ffffff00',  # cyan
          'ff00ffff',  # yellow
          'ff0088ff',  # orange
          'ffff0000',  # blue
          ]

def setLineStyles():
    defaultLineStyle = LineStyle.objects.get(id=1)
    defaultIconStyle = IconStyle.objects.get(id=1)
    for i, track in enumerate(Track.objects.all()):
        color = COLORS[i % len(COLORS)]

        lineStyle = LineStyle(name=track.name,
                              color=color,
                              width=defaultLineStyle.width)
        lineStyle.save()

        iconStyle = IconStyle(name=track.name,
                              url=defaultIconStyle.url,
                              width=defaultIconStyle.width,
                              height=defaultIconStyle.height,
                              scale=defaultIconStyle.scale,
                              color=color)
        iconStyle.save()

        track.lineStyle = lineStyle
        track.iconStyle = iconStyle
        track.save()

def main():
    import optparse
    parser = optparse.OptionParser('usage: %prog')
    opts, args = parser.parse_args()
    if args:
        parser.error('expected no args')
    setLineStyles()

if __name__ == '__main__':
    main()
