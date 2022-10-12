package com.puja.main.service;

import java.util.List;
import java.util.Optional;

import com.puja.main.entities.User;

public interface UserInterface {
	
	User createUser(User user);
	String deleteUser(Long userId);
	User updateUser(Long userId, User userNew);
	List<User> getUsers();
	Optional<User> getOneUser(Long userId);
}
