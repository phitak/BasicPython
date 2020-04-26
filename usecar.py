from Car import*

# สร้าง Object หรือ Instance ของ Class Car
object1 = Car('red', 'Toyota', 4, 4, 180)
object1.printdata()

print()

object2 = Car("", "", 0, 0, 0)
object2.setbrand = "Honda"
object2.setcolor = "Yellow"
object2.setspeed = 200

object2.printdata()
