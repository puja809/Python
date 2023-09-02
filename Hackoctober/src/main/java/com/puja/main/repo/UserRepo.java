package com.puja.main.repo;

import org.springframework.data.jpa.repository.JpaRepository;

import com.puja.main.entities.User;

public interface UserRepo extends JpaRepository<User, Long>{
	
}
