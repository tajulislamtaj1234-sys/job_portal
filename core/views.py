from django.shortcuts import render
from django.views import View


class HomeView(View):

    def get(self, request):

        jobs = [

            {
                "title": "Python Django Developer",
                "company": "Google",
                "location": "Tokyo, Japan",
                "type": "Full Time",
            },

            {
                "title": "Frontend Developer",
                "company": "Microsoft",
                "location": "Osaka, Japan",
                "type": "Remote",
            },

            {
                "title": "Backend Developer",
                "company": "C.A.L",
                "location": "Minato, Japan",
                "type": "Part Time",
            },

            {
                "title": "DevOps Engineer",
                "company": "Amazon",
                "location": "Tokyo",
                "type": "Contract",
            },

            {
                "title": "AI Engineer",
                "company": "OpenAI Japan",
                "location": "Kyoto",
                "type": "Internship",
            }


        ]

        context = {

            "jobs": jobs,

        }

        return render(request, "home.html", context)