package com.puja.main.controller;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.puja.main.entities.User;
import com.puja.main.service.UserInterface;

@CrossOrigin
@RestController
public class UserController {
		
	@Autowired 
	UserInterface userService;
	
	@GetMapping(path="/user/{id}",produces= {"application/json"})
	public Optional<User> getOneUserById(@PathVariable(value="id") Long aid)
	{
		return userService.getOneUser(aid);
	}
	@GetMapping(path="/user",produces= {"application/json"})
	public List<User> getUsers()
	{
		return userService.getUsers();
	}
	@PutMapping(path="/user/{id}",produces= {"application/json"})
	public User updateUserById(@PathVariable(value="id") Long aid,@RequestBody User user)
	{
		return userService.updateUser(aid,user);
	}
	@DeleteMapping(path="/user/{id}",produces= {"application/json"})
	public String deleteUserById(@PathVariable(value="id") Long aid)
	{
		return userService.deleteUser(aid);
	}
	@PostMapping(path="/user",produces= {"application/json"})
	public User updateUserById(@RequestBody User user)
	{
		return userService.createUser(user);
	}
}
