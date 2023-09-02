package com.puja.main.service.impl;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.puja.main.entities.User;
import com.puja.main.repo.UserRepo;
import com.puja.main.service.UserInterface;

@Service
public class UserInterfaceImpl implements UserInterface{

	@Autowired
	UserRepo userRepo;	
	
	@Override
	public User createUser(User user) {
		return userRepo.save(user);
	}

	@Override
	public String deleteUser(Long userId) {
		try {
			userRepo.deleteById(userId);
			return "Delete Success";
		} catch (Exception e) {
			return "Delete Failed";
		}
	}

	@Override
	public User updateUser(Long userId, User userNew) {
		User us = userRepo.findById(userId).orElseThrow(RuntimeException::new);
		us.setName(userNew.getName());
		us.setAddress(userNew.getAddress());
		return userRepo.save(us);
	}

	@Override
	public List<User> getUsers() {
		return userRepo.findAll();
	}

	@Override
	public Optional<User> getOneUser(Long id) {
		return userRepo.findById(id);
	}

}
