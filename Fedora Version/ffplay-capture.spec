Name:           capture-card-app
Version:        1.1
Release:        %autorelease
Summary:        Capture Card App
Source:         %{name}-%{version}.tar.gz
License:        Open
BuildArch:      noarch

%description
Capture Card App written in python. Using GTK and Gst


%prep
%autosetup

%install
install -D -m 0644 capture_card_app.desktop %{buildroot}/usr/share/applications/capture_card_app.desktop
install -D -m 0755 capture_card_app %{buildroot}/usr/bin/capture_card_app
install -D -m 0644 capture-card-app-256x256.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/capture-card-app.png
install -D -m 0644 capture-card-app-48x48.png %{buildroot}/usr/share/icons/hicolor/48x48/apps/capture-card-app.png
%files
/usr/share/applications/capture_card_app.desktop
/usr/share/icons/hicolor/256x256/apps/capture-card-app.png
/usr/share/icons/hicolor/48x48/apps/capture-card-app.png
/usr/bin/capture_card_app

%changelog
%autochangelog
