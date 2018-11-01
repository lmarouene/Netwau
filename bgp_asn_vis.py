##Make sure to install visualize package pip install bgp_visualize
from bgp_visualize import bgp_visualize_asn
ASNs= bgp_visualize_asn.bgp_visualize(asns=[8452,24835],dark=True)
ASNs.Draw()
