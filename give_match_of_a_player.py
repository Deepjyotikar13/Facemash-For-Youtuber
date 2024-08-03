
def give_match_of_a_player_by_ind(yt_ind_t_match,player_ind_t_match):
	player_ind=player_ind_t_match[0] #player index
	player_total_match=player_ind_t_match[1]#total match played by the player
	for person1 in [player_ind]:
		for person_ind_at_0 in yt_ind_t_match[person1+(player_total_match+1):]:
			return [person1,person_ind_at_0[0]]

if __name__=="__main__":
	print(give_match_of_a_player_by_ind(player_index,[0,22],23))
	