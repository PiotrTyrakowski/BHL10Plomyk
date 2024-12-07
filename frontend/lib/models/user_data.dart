import 'package:frontend/models/badge_data.dart';
import 'package:frontend/models/event_categories_enum.dart';
import 'package:frontend/models/event_data.dart';
import 'package:frontend/models/lyf_hotels_enum.dart';

class User {
  final String firstName;
  final String lastName;
  final int age;
  final LyfHotels hotel = LyfHotels.Funan;
  final String profilePic; // = 'images/profile/default_profile_pic.png';
  final String location;
  final bool isManager;
  String? bio;
  List<BadgeData> userBadges;
  Set<EventCategory> preferences = {};
  List<Event> createdEvents = [];
  List<Event> registeredEvents = [];

  User({
    required this.firstName,
    required this.lastName,
    required this.age,
    required this.location,
    required this.profilePic,
    required this.userBadges,
    this.isManager = false,
    this.bio,
    Set<EventCategory>? preferences,
  }) : preferences = preferences ?? {};
}
