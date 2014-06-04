%define debug_package %{nil}

Summary:	Sci-fi RTS and FPS game
Name:		unvanquished-maps
Version:	0.28.0
Release:	1
License:	CC-BY-SA-2.5 and CC-BY-SA-3.0
Group:		Games/Arcade
Url:		https://github.com/Unvanquished/Unvanquished/blob/v%{version}/debian/configfiles/maprotation.cfg
# Update  every single source link, at package update.
Source0:	http://www.unvanquished.net/downloads/pkg/map-UTCS_trem.pk3
Source1:	http://www.unvanquished.net/downloads/pkg/map-arachnid2_trem.pk3
Source2:	http://www.unvanquished.net/downloads/pkg/map-chasm_b1.pk3
Source3:	http://www.unvanquished.net/downloads/pkg/map-forlorn_a4.pk3
Source4:	http://www.unvanquished.net/downloads/pkg/map-karith_trem.pk3
Source5:	http://www.unvanquished.net/downloads/pkg/map-methane-beta1_trem.pk3
Source6:	http://www.unvanquished.net/downloads/pkg/map-nano_trem.pk3
Source7:	http://www.unvanquished.net/downloads/pkg/map-nexus6_trem.pk3
Source8:	http://www.unvanquished.net/downloads/pkg/map-niveus_trem.pk3
Source9:	http://www.unvanquished.net/downloads/pkg/map-orion_trem.pk3
Source10:	http://www.unvanquished.net/downloads/pkg/map-parpax_d02d.pk3
Source11:	http://www.unvanquished.net/downloads/pkg/map-perseus_b4d.pk3
Source12:	http://www.unvanquished.net/downloads/pkg/map-plat23_b11.pk3
Source13:	http://www.unvanquished.net/downloads/pkg/map-plat23_b11+1.pk3
Source14:	http://www.unvanquished.net/downloads/pkg/map-spacetracks-r1_trem.pk3
Source15:	http://www.unvanquished.net/downloads/pkg/map-station15-r1_trem.pk3
Source16:	http://www.unvanquished.net/downloads/pkg/map-thunder_b3.pk3
Source17:	http://www.unvanquished.net/downloads/pkg/map-tremor_trem.pk3
Source18:	http://www.unvanquished.net/downloads/pkg/map-yocto_b2a+1.pk3
Requires:	unvanquished >= %{version}
BuildArch:	noarch

%description
Players fight online in team based combat in a war of aliens against humans.
This package only contains the map pack.

%files
%dir %{_datadir}/unvanquished
%dir %{_datadir}/unvanquished/pkg/
%{_datadir}/unvanquished/pkg/*.pk3

#----------------------------------------------------------------------------

%prep

%build

%install
mkdir -p  %{buildroot}%{_datadir}/unvanquished/pkg/
install -m0644 %{SOURCE0} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE1} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE2} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE3} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE4} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE5} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE6} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE7} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE8} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE9} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE10} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE11} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE12} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE13} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE14} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE15} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE16} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE17} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE18} "%{buildroot}%{_datadir}/unvanquished/pkg/"

