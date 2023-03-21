from numpy import testing

def test_module_import():
	try:
		import mymodule.sky_sim
	except Exception as e:
		raise AssertionError("Failed to import mymodule")
	return
def test_get_radec():
	from mymodule import sky_sim
	answer = (14.215420962967535, 41.26916666666667)
	result = sky_sim.get_radec()
	testing.assert_allclose(answer, result, atol=1./3600)
	return
