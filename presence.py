#! /usr/bin/python

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

class PresenterWindow(QWidget):
    def __init__(self, parent, title="Presence - Presenter"):
        super(PresenterWindow, self).__init__(parent)

        self.setWindowTitle(title)
        
        layout = QVBoxLayout()
        self.webview = QWebView()
        layout.addWidget(self.webview)
        self.setLayout(layout)

        self.pass_events = False
        
    def attach(self, audience_window):
        print "Attached audience window."
        self.partner = audience_window

    def keyPressEvent(self, event):
        super(PresenterWindow, self).keyPressEvent(event)

        if event.key() == Qt.Key_Escape:
            sys.exit(0)

        if self.pass_events:
            print "Passed event"
            self.partner.webview.event(event)
        else:
            print "Passing events."
            self.pass_events = True

class AudienceWindow(QWidget):
    def __init__(self, parent, title="Presence - Audience"):
        super(AudienceWindow, self).__init__(parent)

        self.setWindowTitle(title)
        
        layout = QVBoxLayout()
        self.webview = QWebView()
        layout.addWidget(self.webview)
        self.setLayout(layout)

def show_presentation(presenter, audience, presentation):
    url = QUrl(presentation)
    presenter.webview.load(url)
    audience.webview.load(url)
    presenter.attach(audience)

def main():
    if len(sys.argv) != 2:
        print "Incorrect number of arguments."
        sys.exit(1)

    app = QApplication(sys.argv)
    audience_window = AudienceWindow(None)
    presenter_window = PresenterWindow(None)
    presenter_window.show()
    audience_window.show()

    show_presentation(presenter_window, audience_window, sys.argv[1])
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
