---
id: week-1-ros2-core-concepts
title: ہفتہ 1 ROS2 بنیادی تصورات
---

## ROS 2 ٹاپکس: غیر مطابقت پذیر ڈیٹا اسٹریمز

ROS 2 میں، **ٹاپکس** نوڈس کے درمیان غیر مطابقت پذیر، کئی سے کئی مواصلت کا بنیادی طریقہ کار ہیں۔ ایک ٹاپک کو ایک عوامی اعلاناتی نظام یا ریڈیو اسٹیشن سمجھیں: ایک نوڈ معلومات "براڈکاسٹ" (پبلش) کر سکتا ہے یہ جانے بغیر کہ کون سن رہا ہے، اور کوئی بھی دلچسپی رکھنے والا نوڈ اس معلومات کو وصول کرنے کے لیے "ٹون ان" (سبسکرائب) کر سکتا ہے۔ یہ پیٹرن مسلسل ڈیٹا اسٹریمز جیسے سینسر ریڈنگز، جوائنٹ اسٹیٹس، یا تشخیصی معلومات کے لیے مثالی ہے۔

### ڈیٹا فلو اور پیغام کی اقسام

ٹاپکس پر مواصلت کردہ ڈیٹا **پیغامات** میں منظم ہوتا ہے۔ ہر ٹاپک کے ساتھ ایک مخصوص *پیغام کی قسم* وابستہ ہوتی ہے، جو بھیجی جانے والی معلومات کی ساخت اور ڈیٹا فیلڈز کی وضاحت کرتی ہے۔ مثال کے طور پر، `sensor_msgs/msg/LaserScan` پیغام کی قسم لیزر اسکین ڈیٹا کے لیے فیلڈز کی وضاحت کرے گی، جبکہ `std_msgs/msg/String` پیغام کی قسم صرف ایک سٹرنگ پر مشتمل ہوگی۔ کسی دیے گئے ٹاپک کے لیے پبلشرز اور سبسکرائبرز *ضروری* ہے کہ پیغام کی قسم پر متفق ہوں۔ یہ ڈیٹا کی مستقل مزاجی اور مناسب تشریح کو یقینی بناتا ہے۔

### سروس کا معیار (QoS) سیٹنگز

ROS 2 **سروس کے معیار (QoS) پالیسیاں** متعارف کراتا ہے تاکہ نوڈس کے درمیان پیغامات کا تبادلہ کیسے ہوتا ہے اس پر زیادہ کنٹرول فراہم کیا جا سکے۔ QoS سیٹنگز آپ کو قابل اعتمادی، پیغام کی تاریخ، اور استحکام جیسے پہلوؤں کو ترتیب دینے کی اجازت دیتی ہیں، جو مختلف ایپلی کیشن کی ضروریات کے لیے اہم ہیں۔

مثال کے طور پر:
-   **قابل اعتمادی**: کیا آپ کو ہر پیغام کی ترسیل کی ضرورت ہے (قابل اعتماد) یا اگر نیٹ ورک congested ہے تو کچھ پیغامات کو چھوڑنا ٹھیک ہے (بہترین کوشش)؟
-   **تاریخ**: کیا سبسکرائبر کو پہلے سے جڑنے پر ماضی کے پیغامات وصول کرنے چاہئیں (سب کو برقرار رکھیں) یا صرف حالیہ (آخری کو برقرار رکھیں)؟
-   **استحکام**: کیا پبلشر کو دیر سے شامل ہونے والے سبسکرائبرز کے لیے اپنا آخری پیغام دستیاب کرنا چاہیے (عارضی مقامی) یا صرف فعال سبسکرائبرز کو بھیجنا چاہیے (غیر مستحکم)؟

یہ سیٹنگز ROS 2 کو استعمال کے وسیع پیمانے پر کیسز کو پورا کرنے کے قابل بناتی ہیں، ہائی فریکوئنسی سینسر ڈیٹا سے جو کبھی کبھار نقصان کو برداشت کر سکتا ہے، ان اہم کمانڈ پیغامات تک جن کے لیے ضمانت شدہ ترسیل کی ضرورت ہوتی ہے۔

### پبلشرز: معلومات نشر کرنا

ایک **پبلشر** نوڈ ایک مخصوص ٹاپک پر پیغامات بھیجنے کا ذمہ دار ہوتا ہے۔ یہ تعریف شدہ پیغام کی قسم کی مثالیں بناتا ہے، انہیں ڈیٹا سے بھرتا ہے، اور پھر انہیں "پبلش" کرتا ہے۔ دوسرے نوڈس (سبسکرائبرز) پھر ان پیغامات کو وصول کر سکتے ہیں۔

یہاں ایک `rclpy` پبلشر نوڈ کی مثال ہے:

```python
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from std_msgs.msg import String
import sys
import time

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        # Define a QoS Profile for demonstration
        # BEST_EFFORT means messages might be dropped if network is congested
        # KEEP_LAST with depth 1 means only the most recent message is stored
        # VOLATILE durability means messages are not persisted
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=1,
            durability=DurabilityPolicy.VOLATILE
        )
        self.publisher_ = self.create_publisher(String, 'topic', qos_profile)
        self.i = 0
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info(f'Publisher node "{self.get_name()}" started. Publishing on topic "topic".')

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello ROS 2! Count: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    try:
        rclpy.spin(minimal_publisher)
    except KeyboardInterrupt:
        pass
    finally:
        minimal_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### سبسکرائبرز: معلومات وصول کرنا

ایک **سبسکرائبر** نوڈ ایک مخصوص ٹاپک پر پیغامات کے لیے سنتا ہے۔ جب اس ٹاپک پر ایک پیغام پبلش ہوتا ہے، تو سبسکرائبر اسے وصول کرتا ہے اور ایک کال بیک فنکشن کا استعمال کرتے ہوئے اسے پروسیس کرتا ہے۔ یہ نوڈس کو ROS 2 سسٹم کے دوسرے حصوں کے ذریعے پیدا کردہ واقعات یا ڈیٹا پر ردعمل ظاہر کرنے کی اجازت دیتا ہے۔