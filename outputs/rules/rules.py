def findDecision(obj): #obj[0]: alt, obj[1]: bar, obj[2]: fri, obj[3]: hun, obj[4]: pat, obj[5]: price, obj[6]: rain, obj[7]: res, obj[8]: type, obj[9]: est
	# {"feature": "pat", "instances": 12, "metric_value": 1.0, "depth": 1}
	if obj[4] == 'full':
		# {"feature": "type", "instances": 6, "metric_value": 0.9183, "depth": 2}
		if obj[8] == 'thai':
			# {"feature": "fri", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2] == 'no':
				return 'no'
			elif obj[2] == 'yes':
				return 'yes'
			else: return 'yes'
		elif obj[8] == 'burger':
			# {"feature": "alt", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'no':
				return 'no'
			elif obj[0] == 'yes':
				return 'yes'
			else: return 'yes'
		elif obj[8] == 'french':
			return 'no'
		elif obj[8] == 'italian':
			return 'no'
		else: return 'no'
	elif obj[4] == 'some':
		return 'yes'
	elif obj[4] == 'none':
		return 'no'
	else: return 'no'
