<!DOCTYPE html>
<%@ taglib prefix="spring" uri="http://www.springframework.org/tags"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<html lang="en">
<head>

<link rel="stylesheet" type="text/css"
	href="webjars/bootstrap/3.3.7/css/bootstrap.min.css" />
<c:url value="/css/main.css" var="jstlCss" />
<link href="${jstlCss}" rel="stylesheet" />

</head>
<body>
	<div class="container">
		<header>
			<h1>Spring MVC + JSP + JPA + Spring Boot 2</h1>
		</header>
		<div class="starter-template">
			<h1>Users List</h1>
			<table
				class="table table-striped table-hover table-condensed table-bordered">
				<tr>
					<th>Id</th>
					<th>Train No.</th>
					<th>Source</th>
					<th>Destination</th>
					<th>Date</th>
				</tr>
				<c:forEach var="user" items="${users}">
					<tr>
						<td>${user.id}</td>
						<td>${user.trainNo}</td>
						<td>${user.source}</td>
						<td>${user.destination}</td>
						<td>${user.date}</td>
					</tr>
				</c:forEach>
			</table>
		</div>
		<form:form method="POST" action="/users" modelAttribute="train">
             <table>
                <tr>
                    <td><form:label path="source">Source</form:label></td>
                    <td><form:input path="source"/></td>
                </tr>
                <tr>
                    <td><form:label path="destination">Destination</form:label></td>
                    <td><form:input path="destination"/></td>
                </tr>
                <tr>
                    <td><form:label path="date">Date</form:label></td>
                    <td><form:input path="date"/></td>
                </tr>
                <tr>
                    <td><input type="submit" value="Submit"/></td>
                </tr>
            </table>
        </form:form>
	</div>
	
	<script type="text/javascript"
		src="webjars/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</body>

</html>