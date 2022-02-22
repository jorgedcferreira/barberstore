The Pattern: Ports and Adapters (‘’Object Structural’’) 
Alternative name: ‘’Ports & Adapters’’ 
Alternative name: ‘’Hexagonal Architecture’’


# INTRODUCTION

This report aims at elaborating an analysis about the “Hexagonal Architecture” documented in 2005 by Alistair Cockburn. It is proposed a division into five distinct sections: starting with the context on where this architectural pattern is applied, then the problem that it expects to solve, third one will look behind the hood of the “Hexagonal Architecture” by digesting the solution design and structure, the pros and con analysis will be done with some do’s and don’t and lastly, it will be analyzed a real case of the application of this pattern.


# CONTEXT

The software Loose coupling has been at the center of discussion in the software engineering industry. However there is no solution that fits all and therefore there are contextual aspects, such as organizational structure, business size, or even engineering maturity that can affect the design approach. 
 
In this report, the problem under study will take into account an organizational environment where multiple software engineering teams contribute to the software development, with distinct tech stacks as well as other entities such as users, testing teams, infrastructural engineers, or even automated programs that collaboratively interact with the application. 


# PROBLEM

Within this complex and multi-agent environment, there are two major questions that emerge: how can this dynamic interaction be supported while keeping the system loosely coupled? How can one prevent the infiltration of business logic into the user interface code as the business complexity arises?

These two questions unfold the following consequences: first, systems can’t be tested with automated test suites because part of the business logic is scattered among distinct layers; second, the time to change things like data sources are just too high and complex moreover when multiple teams are working in the same environment, many times monolith structures. 
 


# SOLUTION

Having in mind this scalability challenge, there is an architectural software design that pretends to solve the problem called “The hexagonal architecture”. This pattern follows a visual representation that is based on the following three principles:


- There are two layers at the edges: User/Driving-Side and Server/Driven-Side, 
- At the core one where the Business Logic resides, that won't depend on what is exposed over the edge layers.
- To link edge layers to the core layer, there is an Adapter/Port linkage. 


![](https://blog.octo.com/wp-content/uploads/2020/06/archi_hexa_en_06-1024x526.png)


First, let’s look at the way the edge layers connect with the internal ones. Ports are agnostic entry points from which foreign actors can link to communicate with the application core layer, independently of who is accessing and how the interface was developed. These ports are therefore a set of standard guidelines implemented inside the hexagon to link any interface with the core application. Adapters, on the other hand, are the other side of the ports that are responsible to initiate the interaction by any type of interface to the application.


The application is the core where the business logic code is stored. It contains the domain model, where the business vocabulary is embedded in Aggregates, Entities, and Objects. Ports belong to the inside side of the hexagon and the domain is placed at the center of the geometric figure.


![](https://miro.medium.com/max/700/1*mGLO5IfhJv4o0NYOAZI60A.png)


Now, looking at edge layers, as explained before, they can represent several types of users that can be clustered in two sides: User/Driving side and Server/Driven side.

On the user side, actors like user or external programs will interact with the application, typically expressed by user interface code, JSON serializations to programs, or HTTP routes for an API, by building adapters that use a Port implemented by the application service. Bear in mind that each of these user-side blocks is independent among all the other segments of the outside layer of the hexagon.  

On the Driven side is normally where the infrastructure-related structures reside,  such as the code that interacts with the database, makes calls to the file system, or code that handles HTTP calls to other applications, where therefore the application will find what is requested by the driving side. Driven adapters implement the Port and the application will use it to retrieve the requested details pulled by the Driving side.



# PROS OF THE PATTERN

A Layered Architecture, like the Hexagonal pattern,  has plenty of upsides but there is one that displays greater importance: the clear segregation of responsibilities complexity that a multi-agent organization brings. The implementation of Ports and Adapters allows complete isolation of the application logic and domain logic from the external interactions either user or server-related. Allowing complete independence of the actors that implement the adapters towards standard Ports makes it possible to develop the product interfaces agnostic to the technology. This setup enables distinct software engineering teams to work on the same application, with completely distinct tech stacks without compromising the scalability of the system. 

However, there’s always a risk. As there is no natural mechanism to detect when logic leaks between layers, and it can happen - sometimes more often than expected - where bread crumbs of business logic appear in the user interface or Infrastructure layer.

APPLIED CASES 

Lastly, as the internet becomes the center of how society is evolving, this pattern is becoming more and more frequent, mostly on digital native companies that have displayed impressive growth over the last decade. Netflix is one of them.

Like any other startup, they started with a monolith type of pattern and that decision proved to be right since it allows rapid development and quick changes while the volume of business transactions was not that relevant. But that quickly changed as well, fostered by its exponential growth, Netflix increased to more than 30 developers working in more than 300 database tables. Along with that new business, logic emerged each year bring more and more use cases to support. That was the moment that Netflix decided to move towards service-oriented architecture using the Hexagon pattern. 

The advantages of this approach were revealed in simple things like the need of changing data sources from JSON API to GraphQL in just 2 hours, without compromising the business logic. Another significant impact was around the testing strategy that by implementing this pattern was made compatible with automatic testing tools to all the three layers: user, core, and server-side.

In the end, Netflix believes that the Hexagonal pattern allows them to be technologically agnostic and therefore innovation prone to most of the business problems while keeping an impressive scalable platform.

 



# REFERENCES


como é que o Netflix usa este tipo de arquitetura
https://alistair.cockburn.us/hexagonal-architecture/

https://medium.com/ssense-tech/hexagonal-architecture-there-are-always-two-sides-to-every-story-bc0780ed7d9c


Alistair Cockburn’s original paper on Hexagonal Architecture
Awesome read on Domain-Driven Design: Everything You Always Wanted to Know About it, But Were Afraid to Ask 
Eric Evans’ Domain-Driven Design: Tackling Complexity in the Heart of Software
Bob Martin’s OO Design Quality Metrics
Bob Martin’s Agile Software Development Principles, Patterns and Practices

https://vaadin.com/learn/tutorials/ddd/ddd_and_hexagonal


https://blog.octo.com/hexagonal-architecture-three-principles-and-an-implementation-example/