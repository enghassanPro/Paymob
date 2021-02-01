from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import UserManager

# Define the types of users
TYPE_ACCOUNT_CHOICES = (
    (1, "Admin"),
    (2, "Client"),
)


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.

    The abstract user class use for two types of users. either user admin or normal user
    - if the user is admin, So will store in the type account 1, which mean It's a user admin
    - otherwise will be a normal user. So will store in the type account 2, which means It's a normal user.

    """

    # username field will validate the data that accept letters, digits, -, _ only
    # otherwise will raise error
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and -/_ only.'),
        validators=[RegexValidator(regex="^([a-z]|[a-zA-Z_-]){4,12}$",
                                   message="Enter a valid username. This value may contain only letters, -,_")],
        error_messages={
            'unique': _("A client with that username already exists."),
        },
    )

    # first name field will validate the data that accept letters only
    first_name = models.CharField(_('first name'),
                                  max_length=150,
                                  help_text="should be characters only with max length 50",
                                  validators=[RegexValidator(regex="^[a-zA-Z]+$", message="Enter characters only")])

    # last name field will validate the data that accept letters only
    last_name = models.CharField(_('last name'),
                                 max_length=150,
                                 help_text="should be characters only with max length 50",
                                 validators=[RegexValidator(regex="^[a-zA-Z]+$", message="Enter characters only")])

    email = models.EmailField(_('email address'), unique=True, validators=[EmailValidator])

    phone = models.CharField(max_length=20, unique=True)

    address = models.TextField()

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the client can log into this admin site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this client should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    type_account = models.SmallIntegerField(_("type account"), choices=TYPE_ACCOUNT_CHOICES, null=True)

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('users')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the client."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this client."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_type_account(self):
        return dict(TYPE_ACCOUNT_CHOICES)[self.type_account]


class User(AbstractUser):
    '''
        This Class inherit from the Abstract class
        To use all process of these class
    '''

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
