%define _build_pkgcheck_set %{nil}
%define _build_pkgcheck_srpm %{nil}

Name:           unvanquished-maps
Version:        0.41.0
Release:        1
Summary:        Sci-fi RTS and FPS game
License:        CC-BY-SA-2.5 and CC-BY-SA-3.0
Group:          Games/Arcade
Url:            https://unvanquished.net/

Source1:        http://dl.unvanquished.net/pkg/map-UTCS_trem+1.pk3
Source2:        http://dl.unvanquished.net/pkg/map-arachnid2_trem+1.pk3
Source3:        http://dl.unvanquished.net/pkg/map-karith_trem+1.pk3
Source4:        http://dl.unvanquished.net/pkg/map-methane-beta1_trem+1.pk3
Source5:        http://dl.unvanquished.net/pkg/map-nano_trem+1.pk3
Source6:        http://dl.unvanquished.net/pkg/map-nexus6_trem+1.pk3
Source7:        http://dl.unvanquished.net/pkg/map-niveus_trem+3.pk3
Source8:        http://dl.unvanquished.net/pkg/map-orion_trem+2.pk3
Source9:        http://dl.unvanquished.net/pkg/map-tremor_trem+1.pk3
Source10:       http://dl.unvanquished.net/pkg/map-antares_a04.pk3
Source11:       http://dl.unvanquished.net/pkg/map-chasm_b1+2.pk3
Source12:       http://dl.unvanquished.net/pkg/map-forlorn_a11.pk3
Source13:       http://dl.unvanquished.net/pkg/map-parpax_d04.pk3
Source14:       http://dl.unvanquished.net/pkg/map-perseus_b5a+1.pk3
Source15:       http://dl.unvanquished.net/pkg/map-plat23_b13+1.pk3
Source16:       http://dl.unvanquished.net/pkg/map-spacetracks_1.0+1.pk3
Source17:       http://dl.unvanquished.net/pkg/map-station15_1.0.pk3
Source18:       http://dl.unvanquished.net/pkg/map-thunder_b3+2.pk3
Source19:       http://dl.unvanquished.net/pkg/map-yocto_b2c+1.pk3
Source20:       http://dl.unvanquished.net/pkg/map-antares_a04+1.pk3
Source21:       http://dl.unvanquished.net/pkg/map-forlorn_a12.pk3
Source22:       http://dl.unvanquished.net/pkg/map-parpax_d05.pk3
Source23:       http://dl.unvanquished.net/pkg/map-forlorn_a13~1.pk3
Source24:       http://dl.unvanquished.net/pkg/map-station15_1.0+1.pk3

BuildArch:      noarch
# suggested because I'm not very good on chain build on abf.Symbianflo
Suggests:       unvanquished = %{version}

%description
Players fight online in team based combat 
in a war of aliens against humans.
This package only contains the map pack.
Other maps are available at 
http://dl.unvanquished.net/pkg/,
or automatically downloaded when 
connecting to an online game server.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/unvanquished/pkg/
install -m 644 %{_sourcedir}/map-*.pk3 %{buildroot}%{_datadir}/unvanquished/pkg/

%files
%{_datadir}/unvanquished/pkg/map-*.pk3

