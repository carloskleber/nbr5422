function cxc = arrastoCabos(d)
  cxc(d < 1.5e-3) = 1.2;
  cxc(d >= 1.5e-3) = 1;
end

