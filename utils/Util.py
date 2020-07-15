import torch
class ExperienceBuffer:
	def __init__(self,device,action_space,obs_space):
		self.states = torch.zeros(1,1,obs_space)
		self.rewards = torch.zeros(1,1)	
		self.next_states = torch.zeros(1,obs_space)	
		self.mus = torch.zeros(1,ction_space)	
		self.stds = torch.zeros(1,action_space)	
		self.log_vars = torch.zeros(1,action_space)	
		self.actions = torch.zeros(1,action_space)	
		self.dones = torch.zeros(1,1)
		self.insertion_hist=[]

	def push(self,sate, reward, next_state, mu, std, log_var, action, done,step):
		self.states = torch.cat(self.states,state)
		self.next_states = torch.cat(self.next_states,next_state)
		self.rewards = torch.cat(self.rewards,reward)
		self.mus = torch.cat(self.mus,mu)
		self.stds = torch.cat(self.stds,std)
		self.log_vars = torch.cat(self.log_vars,log_var)
		self.actions = torch.cat(self.actions,action)
		self.dones = torch.cat(self.dones,done)
		self.insertion_hist.append(step)

	def reset(self):
		self.states = torch.zeros(1,1,obs_space)
		self.rewards = torch.zeros(1,1)	
		self.next_states = torch.zeros(1,obs_space)	
		self.mus = torch.zeros(1,ction_space)	
		self.stds = torch.zeros(1,action_space)	
		self.log_vars = torch.zeros(1,action_space)	
		self.actions = torch.zeros(1,action_space)	
		self.dones = torch.zeros(1,1)
		self.insertion_hist=[]

	def pop(self):
		out = [self.states, self,rewards, self.next_states, self.mus, self.stds, self.log_vars, self.actions, self.dones]
		self.reset()
		return out
