def Expected_probability_win(player1_ra,player2_ra,won_or_loss):
	"""
	so if you want to know the probability of your player A winning from (A and B)
	then you should put B(score) the apponent of player A at the place of player1_ra and the actuall player A(score) at the place of player2_ra
	if for player A then Expected_probability_win(playerB_rating,playerA_rating):
		or if for Player B then Expected_probability_win(playerA_rating,playerB_rating):
		
	Ea=1/1+10**((Rb-Ra)/400)
	Eb=1/1+10**((Ra-Rb)/400)
	In ELO Algorithm this formul/algorithm  based on the scores of the two players will predict who has the heigher chance of winning.
	"""
	Current_rating1=player1_ra
	Current_rating2=player2_ra
	Old_rating=player2_ra
	predicted_score=1/(1+10**((Current_rating1-Current_rating2)/400))#predicting formula
	New_score=new_Rating(player2_ra,won_or_loss,predicted_score)#the actual score of players based on if they won or loss
	return predicted_score,int(New_score)
	
	
def new_Rating(old_rating,win_or_loss_point,predicted_win):
	"""So this will give me the score of my player if he has won sore will increse and if he losses then the score will decrease
	"""
	k=27 #as i have 122 player so 27 is a good value for k it would give a moderate change in rating 
	New_Rating=old_rating+k*(win_or_loss_point-predicted_win)
	return New_Rating
if __name__=="__main__":
	#A=Expected_probability_win(1200,1200,0)
	#B=Expected_probability_win(1200,1200,1)
	player_a=1192
	player_b=1208
	ch_a=Expected_probability_win(player_b,player_a,0)#cause i want to to the sckre of player a
	ch_b=Expected_probability_win(player_a,player_b,1)
	print("A",ch_a)
	print("B",ch_b)

	