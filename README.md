# Monitoring-and-segregation-garbage-system
Iot project for segregating and monitoring garbage

An IoT-based garbage monitoring and segregation system with voice control for opening/closing a bin, camera-based animal detection with automated locking, and ultrasonic sensors to track bin fill status. Integrated soil moisture sensor for waste segregation and servo motors to manage bin operations.
Effective waste management has become an imperative concern in contemporary urban settings to mitigate environmental degradation and ensure sustainable development. Garbage segregation plays a pivotal role in this context, aiding in the efficient disposal and recycling of waste materials. This abstract presents the development and implementation of a Garbage Segregation and Monitoring System (GSMS) designed to streamline waste management processes. The GSMS integrates advanced technologies such as Internet of Things (IoT), machine learning, and data analytics to automate and enhance garbage segregation and monitoring practices. Through sensor-equipped bins and smart collection vehicles, the system enables real-time tracking of waste generation, collection, and segregation. 
 
Machine learning algorithms analyze collected data to optimize waste collection, minimize operational costs. Additionally, the system provides actionable insights to municipal authorities for policy formulation and resource allocation. The GSMS not only enhances the efficiency of waste management operations but also promotes public awareness and participation in sustainable waste disposal practices. This abstract highlights the significance of technological interventions in addressing contemporary environmental challenges and underscores the potential of the GSMS in fostering a cleaner and greener urban environment.

Commands:
1. "Open" - opens the lid
2. "Shut" - closes the lid
3. "Level" - gives the level of filled bin (both wet and dry)
   Possible Outputs - Empty, Partially Filled, Full
4. When an animal is shown in the camera - Motor rotates to lock the bin for 10 seconds.
   The bin automatically unlocks after ten seconds, or when the "open" command is said (whichever comes first).

Materials Used:
Hardware:
1. Laptop
2. Arduino UNO
3. Infrared Sensor
4. Ultrasonic Sensor
5. Moisture Sensor
6. Camera
7. Mic
8. Servo Motor
9. Speaker
10. BreadBoard

Software
1. FireBase
2. Flask
3. VOSK
